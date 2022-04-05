from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from core.models import TimestampedModel

class User(AbstractUser, TimestampedModel):
    username = models.CharField(
        _("username"),
        max_length=25,
        unique=True,
        null=False,
        blank=False,
        db_index=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": ("A user with that username already exists")
        }
    )
    email = models.EmailField(
        _("email"),
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        error_messages={
            "unique": ("A user with that email already exists")
        }
    )
    first_name = models.CharField(_("first name"), max_length=100, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=100, blank=False, null=False)
    is_email_verified = models.BooleanField(_("is email verified"), default=False)
    email_verified_at = models.DateTimeField(_("email verified at"), blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.username