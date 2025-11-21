from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class RegisterView(APIView):
    """Register a new user.

    Simple MVP implementation: username, email, password.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return Response(
                {"detail": "username, email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response(
                {"detail": "A user with this username or email already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """Log in a user using username or email and password.

    Uses Django's session authentication under the hood.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        identifier = request.data.get("username") or request.data.get("email")
        password = request.data.get("password")

        if not identifier or not password:
            return Response(
                {"detail": "username/email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = None
        # Try username first
        user = authenticate(request, username=identifier, password=password)
        if user is None:
            # Try email lookup then authenticate with username
            try:
                u = User.objects.get(email=identifier)
            except User.DoesNotExist:
                u = None
            if u is not None:
                user = authenticate(request, username=u.username, password=password)

        if user is None:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.is_active:
            return Response(
                {"detail": "User account is inactive."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        login(request, user)
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """Log out the current user."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeView(generics.RetrieveAPIView):
    """Return the current authenticated user's profile.

    This is a simple starting point; we can later expand to support
    updating profile details.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class MeViewGetOnly(MeView):  # backwards-compatible alias if needed
    def post(self, request, *args, **kwargs):  # pragma: no cover - guard
        return Response(status=405)
