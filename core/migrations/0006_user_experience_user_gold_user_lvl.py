# Generated by Django 4.0.1 on 2022-01-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_character_options_alter_character_base_stats_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='gold',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='user',
            name='lvl',
            field=models.IntegerField(default=1),
        ),
    ]