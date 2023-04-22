from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from app.constants import language_level_choices, part_of_speech_choices


class WordDictionary(models.Model):
    user = models.ManyToManyField(User, related_name="word_dictionaries", verbose_name=_("User"))
    title = models.CharField(max_length=300, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    amount_words = models.IntegerField(default=0, verbose_name=_("Amount of words"))
    author = models.ForeignKey(User, related_name="my_dictionaries", on_delete=models.PROTECT, verbose_name=_("Author"))
    date_of_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date of Create"))
    language_level_from = models.CharField(max_length=2, choices=language_level_choices,
                                           verbose_name=_("Level of Language From"))
    language_level_to = models.CharField(max_length=2, choices=language_level_choices,
                                         verbose_name=_("Level of Language To"))
    vocabulary_analysis = models.JSONField(verbose_name=_("Vocabulary Analysis"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Word Dictionary"
        verbose_name_plural = "Word Dictionaries"
        ordering = ["title", "amount_words"]


class Word(models.Model):
    dictionary = models.ManyToManyField(WordDictionary, related_name="words", verbose_name=_("Dictionary"))
    word = models.CharField(max_length=100, verbose_name=_("Word"))
    root = models.CharField(max_length=30, verbose_name=_("Root"))
    part_of_speech = models.CharField(max_length=15, choices=part_of_speech_choices, verbose_name=_("Part of Speech"))
    russian_value = models.CharField(max_length=100, verbose_name=_("Russian Value"))


def validate_word(word: str) -> None:
    for symbol in word:
        if not symbol.isalpha():
            raise ValidationError("Word can contain only letters")


class LearnedWord(models.Model):
    user = models.ManyToManyField(User, related_name="learned_words", verbose_name=_("User"))
    word = models.CharField(max_length=100, validators=[validate_word], verbose_name=_("Word"))
    root = models.CharField(max_length=100, verbose_name=_("Root"))
    part_of_speech = models.CharField(max_length=20, choices=part_of_speech_choices, verbose_name=_("Part of Speech"))
    russian_value = models.CharField(max_length=100, verbose_name=_("Russian Value"))
