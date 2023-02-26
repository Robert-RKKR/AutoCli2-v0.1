# Generated by Django 4.1.4 on 2023-02-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_globalsetting_is_current_globalsetting_logger_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsetting',
            name='logger_level',
            field=models.IntegerField(choices=[(1, 'CRITICAL'), (2, 'ERROR'), (3, 'WARNING'), (4, 'INFO'), (5, 'DEBUG')], default=1, help_text='The level of severity of the performed action.', verbose_name='Logger severity level'),
        ),
        migrations.AlterField(
            model_name='globalsetting',
            name='notification_level',
            field=models.IntegerField(choices=[(1, 'CRITICAL'), (2, 'ERROR'), (3, 'WARNING'), (4, 'INFO'), (5, 'DEBUG')], default=4, help_text='The level of severity of the performed action.', verbose_name='Notification severity level'),
        ),
    ]