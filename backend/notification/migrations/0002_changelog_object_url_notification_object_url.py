# Generated by Django 4.1.7 on 2023-04-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelog',
            name='object_url',
            field=models.CharField(blank=True, help_text='URL to object.', max_length=1024, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='notification',
            name='object_url',
            field=models.CharField(blank=True, help_text='URL to object.', max_length=1024, null=True, verbose_name='URL'),
        ),
    ]