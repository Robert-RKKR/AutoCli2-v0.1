# Generated by Django 4.1.7 on 2023-03-19 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0018_rename_https_response_execution_http_response_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='executor',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snapshot',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]