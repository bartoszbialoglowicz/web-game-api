# Generated by Django 4.0.1 on 2022-02-06 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_availablequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablequest',
            name='quest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.quest'),
        ),
    ]