from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import stripe

from .models import Course, Lesson, Enrollment, LessonProgress, Order
from .serializers import (
    CourseSerializer,
    LessonSerializer,
    EnrollmentSerializer,
    EnrollmentDetailSerializer,
    OrderSerializer,
)


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for listing and retrieving courses."""

    queryset = Course.objects.filter(is_published=True).order_by("title")
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for lessons.

    Access control:
    - Preview lessons (`is_preview=True`) are public.
    - Non-preview lessons require an active enrollment for the course.
    """

    queryset = Lesson.objects.select_related("course").all()
    serializer_class = LessonSerializer

    def retrieve(self, request, *args, **kwargs):
        lesson = self.get_object()
        # Public preview lessons are always accessible.
        if lesson.is_preview:
            return super().retrieve(request, *args, **kwargs)

        # Non-preview lessons require authentication and active enrollment.
        user = request.user
        if not user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        has_enrollment = Enrollment.objects.filter(
            user=user,
            course=lesson.course,
            status=Enrollment.Status.ACTIVE,
        ).exists()
        if not has_enrollment:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().retrieve(request, *args, **kwargs)


class EnrollmentViewSet(viewsets.ReadOnlyModelViewSet):
    """List and retrieve enrollments for the current user."""

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Enrollment.objects.filter(user=self.request.user)
            .select_related("course")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return EnrollmentDetailSerializer
        return EnrollmentSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="lessons/(?P<lesson_id>[^/.]+)/progress",
    )
    def update_lesson_progress(self, request, pk=None, lesson_id=None):
        """Update completion status for a lesson within this enrollment.

        Endpoint shape matches:
        POST /api/enrollments/{enrollment_id}/lessons/{lesson_id}/progress/
        """

        enrollment = self.get_object()
        if enrollment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        lesson = get_object_or_404(Lesson, pk=lesson_id, course=enrollment.course)
        is_completed = bool(request.data.get("is_completed", False))

        lp, _created = LessonProgress.objects.get_or_create(
            enrollment=enrollment,
            lesson=lesson,
        )
        lp.is_completed = is_completed
        now = timezone.now()
        lp.last_viewed_at = now
        if is_completed and lp.completed_at is None:
            lp.completed_at = now
        if not is_completed:
            lp.completed_at = None
        lp.save()

        return Response({"is_completed": lp.is_completed}, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """List orders for the current user."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .select_related("course")
            .order_by("-created_at")
        )


from rest_framework.views import APIView


class CreateCheckoutSessionView(APIView):
    """Create a Stripe Checkout Session for buying a single course.

    - Creates a local Order record with status `pending`.
    - Creates a Stripe Checkout Session tied to that order.
    - Returns the `session.url` for the frontend to redirect the user.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        course_id = request.data.get("course_id")
        if not course_id:
            return Response(
                {"detail": "course_id is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        course = get_object_or_404(Course, pk=course_id, is_published=True)

        if not settings.STRIPE_SECRET_KEY:
            return Response(
                {"detail": "Stripe is not configured on the server."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        stripe.api_key = settings.STRIPE_SECRET_KEY

        order = Order.objects.create(
            user=request.user,
            course=course,
            amount=course.price,
            currency="USD",
            status=Order.Status.PENDING,
            provider="stripe",
        )

        unit_amount = int(order.amount * 100)

        session = stripe.checkout.Session.create(
            mode="payment",
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": order.currency.lower(),
                        "unit_amount": unit_amount,
                        "product_data": {"name": course.title},
                    },
                    "quantity": 1,
                }
            ],
            metadata={
                "order_id": str(order.id),
                "user_id": str(request.user.id),
                "course_id": str(course.id),
            },
            success_url=f"{settings.FRONTEND_BASE_URL}/payments/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{settings.FRONTEND_BASE_URL}/payments/cancel",
        )

        order.provider_session_id = session.id
        order.save(update_fields=["provider_session_id", "updated_at"])

        return Response(
            {"order_id": order.id, "checkout_url": session.url},
            status=status.HTTP_200_OK,
        )


class OrderWebhookView(APIView):
    """Stripe webhook endpoint to update order status.

    Expects standard Stripe webhook payloads. On `checkout.session.completed`,
    it marks the corresponding Order as `paid` and creates an Enrollment.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if not settings.STRIPE_WEBHOOK_SECRET:
            return Response(
                {"detail": "Stripe webhook secret is not configured."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except (ValueError, stripe.error.SignatureVerificationError):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            metadata = session.get("metadata", {}) or {}
            order_id = metadata.get("order_id")
            if order_id is not None:
                order = get_object_or_404(Order, pk=order_id)
                order.status = Order.Status.PAID
                order.provider_payment_id = session.get("payment_intent")
                order.save(update_fields=["status", "provider_payment_id", "updated_at"])

                if order.course is not None:
                    Enrollment.objects.get_or_create(
                        user=order.user,
                        course=order.course,
                        defaults={"source": Enrollment.Source.PURCHASE},
                    )

        return Response(status=status.HTTP_200_OK)
