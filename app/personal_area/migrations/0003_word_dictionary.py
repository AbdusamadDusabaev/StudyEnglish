# Generated by Django 4.2 on 2023-04-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_area', '0002_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='dictionary',
            field=models.ManyToManyField(related_name='words', to='personal_area.worddictionary', verbose_name='Dictionary'),
        ),
    ]