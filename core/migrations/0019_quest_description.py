# Generated by Django 4.0.1 on 2022-02-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_availablequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]