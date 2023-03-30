# Generated by Django 4.1.7 on 2023-03-26 20:43

import autocli2.base.validators.base_validator
import connector.validators.connection_template_validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionTemplate',
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
                ('execution_protocol', models.IntegerField(choices=[(1, 'SSH'), (2, 'HTTP(S)'), (3, 'Discovery')], default=1, help_text='The network protocol that will be used to execute connection template (SSH / HTTP(S)).', verbose_name='Execution protocol')),
                ('ssh_type', models.IntegerField(choices=[(1, 'SSH command'), (2, 'SSH command template')], default=1, help_text='Type of SSH connection template (Command / template).', verbose_name='SSH execution type')),
                ('ssh_command', models.CharField(blank=True, help_text='The CLI command that will be executed on the remote host.', max_length=128, null=True, verbose_name='CLI command')),
                ('ssh_template', models.TextField(blank=True, help_text='SSh template will be used to create CLI command(s), which will be executed in the remote host to change configuration.', null=True, verbose_name='Template')),
                ('ssh_special_template', models.BooleanField(default=False, help_text='Xxx.', verbose_name='Special template')),
                ('ssh_vrf_template', models.BooleanField(default=False, help_text='VRF cli command template.', verbose_name='VRF template')),
                ('http_method', models.IntegerField(choices=[(1, 'GET'), (2, 'POST'), (3, 'PUT'), (4, 'DELETE')], default=1, help_text='Type of HTTP request method (GET, POST, PUT, DELETE).', verbose_name='HTTP(S) request method')),
                ('http_url', models.CharField(blank=True, help_text='HTTP(S) URL field used to generate API request.', max_length=128, null=True, verbose_name='HTTP(S) URL')),
                ('http_params', models.JSONField(blank=True, help_text='HTTP(S) parameters field used to generate API request.', null=True, verbose_name='HTTP(S) parameters')),
                ('http_body', models.JSONField(blank=True, help_text='HTTP(S) body field used to generate API request.', null=True, verbose_name='HTTP(S) body')),
                ('http_response_type', models.IntegerField(choices=[(0, 'Empty'), (1, 'List'), (2, 'Dict'), (3, 'String')], default=1, help_text='Type of HTTP(S) response. If the host sends a response of a different type than specified, the response will be treated as invalid.', verbose_name='HTTP(s) type of response')),
                ('regex_expression', models.TextField(blank=True, help_text='Regex expression used to validate the output after the execution of the template.', null=True, validators=[connector.validators.connection_template_validators.regex_validator], verbose_name='Regex expression')),
            ],
            options={
                'verbose_name': 'Connection template',
                'verbose_name_plural': 'Connection templates',
            },
        ),
        migrations.CreateModel(
            name='DataGroupTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated')),
                ('keys', models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='Keys')),
                ('keys_regex', models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Keys REGEX')),
                ('connection_template', models.ForeignKey(blank=True, help_text='Connection template.', null=True, on_delete=django.db.models.deletion.PROTECT, to='connector.connectiontemplate', verbose_name='Connection template')),
            ],
            options={
                'verbose_name': 'Data group template',
                'verbose_name_plural': 'Data group templates',
            },
        ),
        migrations.CreateModel(
            name='ModelGroupTemplate',
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
                'verbose_name': 'Model group template',
                'verbose_name_plural': 'Model group templates',
            },
        ),
        migrations.CreateModel(
            name='ModelTemplate',
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
                ('model_group_template', models.ForeignKey(blank=True, help_text='Model group template.', null=True, on_delete=django.db.models.deletion.PROTECT, to='connector.modelgrouptemplate', verbose_name='Model group template')),
            ],
            options={
                'verbose_name': 'Model template',
                'verbose_name_plural': 'Model templates',
            },
        ),
        migrations.CreateModel(
            name='DataTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated')),
                ('path', models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='Path')),
                ('data_group_template', models.ForeignKey(blank=True, help_text='Data group template.', null=True, on_delete=django.db.models.deletion.PROTECT, to='connector.datagrouptemplate', verbose_name='Data group template')),
                ('model_template', models.ForeignKey(blank=True, help_text='Model template.', null=True, on_delete=django.db.models.deletion.PROTECT, to='connector.modeltemplate', verbose_name='Model template')),
            ],
            options={
                'verbose_name': 'Data template',
                'verbose_name_plural': 'Data templates',
            },
        ),
        migrations.AddField(
            model_name='datagrouptemplate',
            name='model_group_template',
            field=models.ForeignKey(blank=True, help_text='Model group template.', null=True, on_delete=django.db.models.deletion.PROTECT, to='connector.modelgrouptemplate', verbose_name='Model group template'),
        ),
    ]