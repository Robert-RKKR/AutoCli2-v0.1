# Generated by Django 4.1.7 on 2023-07-28 12:51

import autocli2.base.validators.base_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated')),
                ('name', models.CharField(error_messages={'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.'}, help_text='IdentificationModel name.', max_length=64, unique=True, validators=[autocli2.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=128, unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, default='IdentificationModel default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='IdentificationModel description.', max_length=256, null=True, validators=[autocli2.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='IdentificationModel graphical representation.', verbose_name='IdentificationModel ico')),
                ('is_current', models.BooleanField(default=True, help_text='Active settings template used by the AutoCli 2 application', verbose_name='Current global settings')),
                ('notification_level', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=4, help_text='The level of severity of the performed action.', verbose_name='Notification severity level')),
                ('logger_level', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=1, help_text='The level of severity of the performed action.', verbose_name='Logger severity level')),
                ('default_user', models.CharField(default='admin', help_text='Default username used to connect to hosts.', max_length=128, verbose_name='Default username')),
                ('default_password', models.CharField(default='!Cisco@12345', help_text='Default password used to connect to hosts.', max_length=128, verbose_name='Default password')),
                ('http_timeout', models.IntegerField(default=10, help_text='The HTTP(S) timeout refers to the time that an AutoCli 2 application waits for a response to an HTTP(S) request before closing the connection.', verbose_name='HTTP session timeout')),
                ('ssh_timeout', models.IntegerField(default=10, help_text='The SSH timeout refers to the time that an AutoCli 2 application waits for a response to an SSH request before closing the connection.', verbose_name='SSH session timeout')),
                ('ssh_repeat', models.IntegerField(default=2, help_text='The SSH repeat connection refers to the number of repeats that the application will make in case the previous one fails.', verbose_name='SSH repeat connection')),
                ('ssh_invalid_responses', models.JSONField(default=['% Invalid input detected', 'syntax error, expecting', 'Error: Unrecognized command', '%Error', 'command not found', 'Syntax Error: unexpected argument', '% Unrecognized command found at', 'invalid input detected', 'cdp is not enabled', 'incomplete command', 'no spanning tree instance exists', 'lldp is not enabled', 'snmp agent not enabled'], help_text='List of strings that contain invalid host responses. For example, the Cisco IOS system returns output such as "invalid input detected" in the case of an unsupported command, or "cdp is not enabled" in the case of an disabled function, in this example CDP.', verbose_name='SSH invalid responses')),
            ],
            options={
                'verbose_name': 'Global settings',
                'verbose_name_plural': 'Global settings',
            },
        ),
    ]
