from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "email", "date_of_registration", "first_name", "second_name", "progress_points",
                    "amount_read_words", "amount_read_articles", "language_level")
    list_display_links = ("id", "user", "email")
