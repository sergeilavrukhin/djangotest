# Generated by Django 2.2.8 on 2021-09-19 08:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210919_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmovements',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountmovements',
            name='time_created',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
