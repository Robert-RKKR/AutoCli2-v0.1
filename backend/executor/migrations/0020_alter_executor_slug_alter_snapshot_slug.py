# Generated by Django 4.1.7 on 2023-03-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0019_executor_slug_snapshot_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='slug',
            field=models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=512, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='slug',
            field=models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=512, unique=True, verbose_name='Slug'),
        ),
    ]
