from django.contrib import admin
from .models import Word, WordDictionary, LearnedWord


@admin.register(WordDictionary)
class WordDictionaryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "amount_words", "author", "date_of_create",
                    "language_level_from", "language_level_to", "vocabulary_analysis")
    list_display_links = ("id", "title")


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "root", "part_of_speech", "russian_value")
    list_display_links = ("id", "word", "root")


@admin.register(LearnedWord)
class LearnedWordAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "root", "part_of_speech", "russian_value")
    list_display_links = ("id", "word", "root")
