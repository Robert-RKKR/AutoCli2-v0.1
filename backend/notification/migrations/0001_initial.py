# Generated by Django 4.1.7 on 2023-03-31 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Time of the change creation.', verbose_name='Timestamp')),
                ('action_type', models.IntegerField(choices=[(0, 'Empty'), (1, 'Create'), (2, 'Update'), (3, 'Delete')], default=0, help_text='The type of action that was performed on the object.', verbose_name='Type of action')),
                ('app_name', models.CharField(blank=True, help_text='Name of the object application.', max_length=64, null=True, verbose_name='Object application name')),
                ('model_name', models.CharField(blank=True, help_text='Name of the object model.', max_length=64, null=True, verbose_name='Object model name')),
                ('object_id', models.IntegerField(blank=True, help_text='Correlated object PK representation.', null=True, verbose_name='Object PK')),
                ('object_representation', models.CharField(blank=True, help_text='Object representation.', max_length=128, null=True, verbose_name='Object representation')),
                ('execution_time', models.FloatField(blank=True, help_text='Log execution time.', null=True, verbose_name='Execution time')),
                ('severity', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=0, help_text='The level of severity of the performed action.', verbose_name='Severity level')),
                ('notification_type', models.IntegerField(choices=[(1, 'User notification'), (2, 'Backend log')], default=1, help_text='Type of notification (User / backlog).', verbose_name='Notification type')),
                ('task_id', models.CharField(blank=True, help_text='ID of the associated task.', max_length=64, null=True, verbose_name='Task ID')),
                ('application', models.CharField(help_text='Name of the application which triggered the notification.', max_length=64, verbose_name='Application')),
                ('message', models.CharField(error_messages={'invalid': 'Enter a valid Notification message. It must contain 1 to 1024 digits.'}, help_text='Notification message.', max_length=1024, verbose_name='Message')),
                ('administrator', models.ForeignKey(blank=True, help_text='Administrator responsible for provided change.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Administrator')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Time of the change creation.', verbose_name='Timestamp')),
                ('action_type', models.IntegerField(choices=[(0, 'Empty'), (1, 'Create'), (2, 'Update'), (3, 'Delete')], default=0, help_text='The type of action that was performed on the object.', verbose_name='Type of action')),
                ('app_name', models.CharField(blank=True, help_text='Name of the object application.', max_length=64, null=True, verbose_name='Object application name')),
                ('model_name', models.CharField(blank=True, help_text='Name of the object model.', max_length=64, null=True, verbose_name='Object model name')),
                ('object_id', models.IntegerField(blank=True, help_text='Correlated object PK representation.', null=True, verbose_name='Object PK')),
                ('object_representation', models.CharField(blank=True, help_text='Object representation.', max_length=128, null=True, verbose_name='Object representation')),
                ('execution_time', models.FloatField(blank=True, help_text='Log execution time.', null=True, verbose_name='Execution time')),
                ('after', models.JSONField(blank=True, help_text='JSON object representation after changes was made, and saved to database.', null=True, verbose_name='JSON object representation')),
                ('administrator', models.ForeignKey(blank=True, help_text='Administrator responsible for provided change.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Administrator')),
            ],
            options={
                'verbose_name': 'Change',
                'verbose_name_plural': 'Changes',
                'ordering': ['-pk'],
            },
        ),
    ]
