# Generated by Django 4.1.7 on 2023-04-08 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0016_alter_crontabschedule_timezone'),
        ('executor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='executor',
            name='interval',
            field=models.ForeignKey(blank=True, help_text='Interval Schedule to run the task on.  Set only one schedule type, leave the others null.', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.intervalschedule', verbose_name='Interval Schedule'),
        ),
    ]