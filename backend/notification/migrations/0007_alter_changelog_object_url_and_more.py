# Generated by Django 4.1.7 on 2023-04-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_alter_changelog_object_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='object_url',
            field=models.CharField(blank=True, help_text='URL to object.', max_length=256, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='object_url',
            field=models.CharField(blank=True, help_text='URL to object.', max_length=256, null=True, verbose_name='URL'),
        ),
    ]