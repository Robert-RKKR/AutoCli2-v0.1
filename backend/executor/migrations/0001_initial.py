# Generated by Django 4.1.7 on 2023-03-26 20:43

import autocli2.base.validators.base_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated')),
                ('value', models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Value')),
                ('json_value', models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='JSON value')),
            ],
            options={
                'verbose_name': 'Converted data',
                'verbose_name_plural': 'Converted data',
            },
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated')),
                ('host_representation', models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Host representation')),
                ('connection_template_representation', models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Connection template representation')),
                ('credential_representation', models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Credential representation')),
                ('task_id', models.CharField(blank=True, help_text='ID of the associated task.', max_length=64, null=True, verbose_name='Task ID')),
                ('execution_status', models.BooleanField(default=False, help_text='A positive result means that the command output was successfully received and processed.', verbose_name='Execution status')),
                ('ssh_raw_data_status', models.BooleanField(default=False, help_text='A positive result means that the raw data collection process has been successfully completed.', verbose_name='SSH raw data status')),
                ('ssh_processed_data_status', models.BooleanField(default=False, help_text='A positive result means that the process of processing the data was completed successfully.', verbose_name='SSH processed data status')),
                ('ssh_raw_data', models.TextField(blank=True, help_text='CLI command raw data output.', null=True, verbose_name='SSH command raw data')),
                ('ssh_processed_data', models.JSONField(blank=True, help_text='CLI command FSM process data.', null=True, verbose_name='SSH command processed data')),
                ('http_response_code', models.IntegerField(blank=True, help_text='Xxx.', null=True, verbose_name='HTTP(S) response code')),
                ('http_response', models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='HTTP(S) response')),
            ],
            options={
                'verbose_name': 'Execution',
                'verbose_name_plural': 'Executions',
            },
        ),
        migrations.CreateModel(
            name='Executor',
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
                ('executor_type', models.IntegerField(choices=[(1, 'Task'), (2, 'Template/s')], default=1, help_text='Xxx.', verbose_name='Executor type')),
                ('task', models.IntegerField(choices=[(1, 'Collect host/s data'), (2, 'Check host/s status')], default=0, help_text='Xxx.', verbose_name='Task')),
                ('task_arguments', models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='Task arguments')),
            ],
            options={
                'verbose_name': 'Executor',
                'verbose_name_plural': 'Executors',
            },
        ),
        migrations.CreateModel(
            name='Snapshot',
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
            ],
            options={
                'verbose_name': 'Snapshot',
                'verbose_name_plural': 'Snapshots',
            },
        ),
    ]