# Generated by Django 4.0.1 on 2022-02-06 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_quest_character_reward_alter_quest_item_reward'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
