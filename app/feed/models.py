from django.db import models
from django.utils.translation import gettext_lazy as _
from app.constants import language_level_choices


class Article(models.Model):
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    source = models.CharField(max_length=100, verbose_name=_("Source"))
    reading_time = models.CharField(max_length=100, verbose_name=_("Reading Time"))
    amount_views = models.IntegerField(default=0, verbose_name=_("Amount of Views"))
    language_level = models.CharField(max_length=2, choices=language_level_choices, verbose_name=_("Level of Language"))
    likes = models.IntegerField(default=0, verbose_name=_("Amount of Likes"))
    dislikes = models.IntegerField(default=0, verbose_name=_("Amount of Dislikes"))
    date_of_publication = models.DateTimeField(auto_now_add=True, verbose_name=_("Date of publication"))
    topic = models.ForeignKey("Topic", on_delete=models.PROTECT, verbose_name=_("Topic of Article"))
    tags = models.ManyToManyField("Tag", verbose_name=_("Tags"))
    style = models.ManyToManyField("Style", verbose_name=_("Style"))
    vocabulary_analysis = models.JSONField(verbose_name=_("Vocabulary Analysis"))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        default_related_name = "articles"
        ordering = ["date_of_publication"]


class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    amount_objects = models.IntegerField(default=0, verbose_name=_("Amount of Objects"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article Topic"
        verbose_name_plural = "Article Topics"
        ordering = ["title"]


class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    amount_objects = models.IntegerField(default=0, verbose_name=_("Amount of Objects"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["title"]


class Style(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    amount_objects = models.IntegerField(default=0, verbose_name=_("Amount of objects"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Styles"
        ordering = ["title"]


