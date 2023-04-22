from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from app.constants import language_level_choices


def get_user_avatar_image_path(instance: "Profile", filename: str) -> str:
    new_filename = "avatar.jpeg"
    return f"users/user-{instance.pk}/{new_filename}"


def validate_first_name(first_name: str) -> None:
    validate_name(name=first_name, field_name="First Name")


def validate_second_name(second_name: str) -> None:
    validate_name(name=second_name, field_name="Second Name")


def validate_name(name: str, field_name: str) -> None:
    for symbol in name:
        if not symbol.isalpha():
            raise ValidationError(f"Field {field_name} must contains only letters")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name=_("User"))
    avatar = models.ImageField(upload_to=get_user_avatar_image_path, verbose_name=_("Avatar"))
    email = models.EmailField(null=True, verbose_name=_("Email"))
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name=_("Date of registration"))
    first_name = models.CharField(max_length=100, null=True, validators=[validate_first_name],
                                  verbose_name=_("First Name"))
    second_name = models.CharField(max_length=100, null=True, validators=[validate_second_name],
                                   verbose_name=_("Second Name"))
    progress_points = models.IntegerField(default=0, verbose_name=_("Progress Points"))
    amount_read_words = models.BigIntegerField(default=0, verbose_name=_("Amount of Read Words"))
    amount_read_articles = models.IntegerField(default=0, verbose_name=_("Amount of Read Articles"))
    language_level = models.CharField(max_length=2, default="A1", choices=language_level_choices,
                                      verbose_name=_("Level of Language"))

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
