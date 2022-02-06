# Generated by Django 4.0.1 on 2022-02-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_quest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='character_reward',
            field=models.ManyToManyField(blank=True, to='core.Character'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='item_reward',
            field=models.ManyToManyField(blank=True, to='core.Item'),
        ),
    ]
