# Generated by Django 3.2.9 on 2021-11-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]