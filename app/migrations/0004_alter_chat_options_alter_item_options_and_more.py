# Generated by Django 4.2.4 on 2023-08-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name_plural': 'Chat'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Item'},
        ),
        migrations.AlterModelOptions(
            name='item_tag',
            options={'verbose_name_plural': 'Item_Tag'},
        ),
        migrations.AlterModelOptions(
            name='matching',
            options={'verbose_name_plural': 'Matching'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Review'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Tag'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddConstraint(
            model_name='matching',
            constraint=models.UniqueConstraint(fields=('buyer_id', 'item_id'), name='buyer_item_unique'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('rater_id', 'evaluator_id'), name='rater_evaluator_unique'),
        ),
    ]
