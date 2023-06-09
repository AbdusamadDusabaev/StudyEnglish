# Generated by Django 4.2 on 2023-04-14 22:22

from django.conf import settings
from django.db import migrations, models
import personal_area.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal_area', '0004_remove_worddictionary_user_worddictionary_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worddictionary',
            name='user',
            field=models.ManyToManyField(related_name='word_dictionaries', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='LearnedWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, validators=[personal_area.models.validate_word], verbose_name='Word')),
                ('root', models.CharField(max_length=100, verbose_name='Root')),
                ('part_of_speech', models.CharField(choices=[('Verb', 'Verb'), ('Adverb', 'Adverb'), ('Adjective', 'Adjective'), ('Noun', 'Noun'), ('Pronoun', 'Pronoun'), ('Participle', 'Participle'), ('Preposition', 'Preposition'), ('Numeral', 'Numeral'), ('Particle', 'Particle'), ('Conjunction', 'Conjunction')], max_length=20, verbose_name='Part of Speech')),
                ('user', models.ManyToManyField(related_name='learned_words', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
