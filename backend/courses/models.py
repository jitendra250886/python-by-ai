from django.db import models
from django.conf import settings


class Course(models.Model):
    """Represents a course in the Python Master Course platform."""

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        help_text="Price of the course in the default currency (e.g. USD).",
    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return self.title


class Lesson(models.Model):
    """A single lesson within a course.

    For now, we keep this simple: each lesson belongs directly to a course
    and stores ordering plus a content path that can point to generated
    markdown/HTML content.
    """

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)
    content_path = models.CharField(
        max_length=500,
        help_text=(
            "Relative path to the rendered lesson content (e.g. "
            "'generated_content/beginner/lesson-01.html')."
        ),
    )
    is_preview = models.BooleanField(
        default=False,
        help_text="Whether this lesson is available to non-enrolled users.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["course", "order"]
        unique_together = ("course", "order")

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return f"{self.course.title} - {self.title}"


class Enrollment(models.Model):
    """Represents a student's access to a course."""

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        CANCELLED = "cancelled", "Cancelled"
        EXPIRED = "expired", "Expired"

    class Source(models.TextChoices):
        PURCHASE = "purchase", "Purchase"
        MANUAL = "manual", "Manual"
        ADMIN_GRANT = "admin_grant", "Admin Grant"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    source = models.CharField(
        max_length=20,
        choices=Source.choices,
        default=Source.PURCHASE,
    )
    started_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return f"Enrollment(user={self.user_id}, course={self.course_id})"


class LessonProgress(models.Model):
    """Tracks progress of a lesson within an enrollment."""

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="lesson_progress",
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_viewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("enrollment", "lesson")

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return f"LessonProgress(enrollment={self.enrollment_id}, lesson={self.lesson_id})"


class Order(models.Model):
    """Represents a payment attempt/transaction for a course."""

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        FAILED = "failed", "Failed"
        REFUNDED = "refunded", "Refunded"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10, default="USD")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    provider = models.CharField(
        max_length=50,
        default="stripe",
        help_text="Payment provider used to process the order.",
    )
    provider_session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="ID of the checkout/session object in the payment provider.",
    )
    provider_payment_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="ID of the final payment/charge in the payment provider.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return f"Order(id={self.id}, user={self.user_id}, course={self.course_id}, status={self.status})"
