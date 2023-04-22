# Generated by Django 4.2 on 2023-04-13 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WordDictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('amount_words', models.IntegerField(default=0, verbose_name='Amount of words')),
                ('date_of_create', models.DateTimeField(auto_now_add=True, verbose_name='Date of Create')),
                ('language_level_from', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=2, verbose_name='Level of Language From')),
                ('language_level_to', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=2, verbose_name='Level of Language To')),
                ('vocabulary_analysis', models.JSONField(verbose_name='Vocabulary Analysis')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_dictionary', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Word Dictionary',
                'verbose_name_plural': 'Word Dictionaries',
                'ordering': ['title', 'amount_words'],
            },
        ),
    ]