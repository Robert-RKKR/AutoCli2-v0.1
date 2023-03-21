# Generated by Django 4.1.7 on 2023-03-19 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_credential_is_deleted_remove_host_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]