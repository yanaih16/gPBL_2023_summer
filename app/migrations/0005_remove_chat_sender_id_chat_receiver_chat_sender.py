# Generated by Django 4.2.4 on 2023-08-28 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_chat_options_alter_item_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
