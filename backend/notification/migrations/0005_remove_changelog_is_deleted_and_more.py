# Generated by Django 4.1.7 on 2023-03-23 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0004_changelog_is_deleted_notification_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='changelog',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_deleted',
        ),
        migrations.AlterField(
            model_name='changelog',
            name='administrator',
            field=models.ForeignKey(blank=True, help_text='Administrator responsible for provided message object.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Administrator'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='administrator',
            field=models.ForeignKey(blank=True, help_text='Administrator responsible for provided message object.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Administrator'),
        ),
    ]