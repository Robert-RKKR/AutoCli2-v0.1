# Generated by Django 4.1.7 on 2023-03-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_globalsetting_default_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='api_token',
            field=models.CharField(blank=True, help_text='Token that will be used during API request.', max_length=128, null=True, verbose_name='Token'),
        ),
    ]
