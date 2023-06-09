# Generated by Django 4.2 on 2023-04-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('amount_objects', models.IntegerField(default=0, verbose_name='Amount of Objects')),
            ],
            options={
                'verbose_name': 'Article Topic',
                'verbose_name_plural': 'Article Topics',
                'ordering': ['title'],
            },
        ),
    ]
