# Generated by Django 4.2.4 on 2023-08-30 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_user_id_item_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='receiver',
        ),
        migrations.AddField(
            model_name='chat',
            name='matching_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.matching'),
            preserve_default=False,
        ),
    ]
