from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with a simple role field.

    Using a custom user now avoids painful migrations later when we add
    more platform-specific fields.
    """

    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        INSTRUCTOR = "instructor", "Instructor"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
        help_text="Determines the user's primary role on the platform.",
    )

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return f"{self.username} ({self.role})"
