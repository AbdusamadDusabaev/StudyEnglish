# Generated by Django 4.2 on 2023-04-13 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('source', models.CharField(max_length=100, verbose_name='Source')),
                ('reading_time', models.CharField(max_length=100, verbose_name='Reading Time')),
                ('amount_views', models.IntegerField(default=0, verbose_name='Amount of Views')),
                ('language_level', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=2, verbose_name='Level of Language')),
                ('likes', models.IntegerField(default=0, verbose_name='Amount of Likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='Amount of Dislikes')),
                ('date_of_publication', models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')),
                ('vocabulary_analysis', models.JSONField(verbose_name='Vocabulary Analysis')),
                ('style', models.ManyToManyField(to='feed.style', verbose_name='Style')),
                ('tags', models.ManyToManyField(to='feed.tag', verbose_name='Tags')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feed.topic', verbose_name='Topic of Article')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['date_of_publication'],
                'default_related_name': 'articles',
            },
        ),
    ]