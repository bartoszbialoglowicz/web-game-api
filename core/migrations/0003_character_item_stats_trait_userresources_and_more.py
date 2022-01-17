# Generated by Django 4.0.1 on 2022-01-17 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_is_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('profession', models.CharField(max_length=64)),
                ('power', models.IntegerField()),
                ('tier', models.IntegerField(choices=[('Common', 1), ('Rare', 2), ('Epic', 3), ('Mythic', 4), ('Legendary', 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('tier', models.IntegerField(choices=[('Common', 1), ('Rare', 2), ('Epic', 3), ('Mythic', 4), ('Legendary', 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage', models.IntegerField()),
                ('health', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('resists', models.IntegerField()),
                ('critical_percent', models.IntegerField()),
                ('critical_damge', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characters', models.ManyToManyField(to='core.Character')),
                ('items', models.ManyToManyField(to='core.Item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='base_stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stats'),
        ),
        migrations.AddField(
            model_name='character',
            name='base_stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stats'),
        ),
        migrations.AddField(
            model_name='character',
            name='traits',
            field=models.ManyToManyField(to='core.Trait'),
        ),
    ]