# Generated by Django 4.0.1 on 2022-01-18 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_character_item_stats_trait_userresources_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='profession',
        ),
    ]
