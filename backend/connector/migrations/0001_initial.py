# Generated by Django 4.1.4 on 2023-02-26 13:04

import autocli2.base.validators.base_validator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DataTimeModel create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='DataTimeModel last update date.', verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'IdentificationModel with this name already exists.'}, help_text='IdentificationModel name.', max_length=64, unique=True, validators=[autocli2.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=64, unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, default='IdentificationModel default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='IdentificationModel description.', max_length=256, null=True, validators=[autocli2.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='IdentificationModel graphical representation.', verbose_name='IdentificationModel ico')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is StatusModel deleted (Deleted StatusModel is reserved for backward compatibility).', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is StatusModel root (Root StatusModel cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is StatusModel active (Inactive StatusModel has limited functionality).', verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Connection group',
                'verbose_name_plural': 'Connection groups',
            },
        ),
        migrations.CreateModel(
            name='ConnectionTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DataTimeModel create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='DataTimeModel last update date.', verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'IdentificationModel with this name already exists.'}, help_text='IdentificationModel name.', max_length=64, unique=True, validators=[autocli2.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=64, unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, default='IdentificationModel default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='IdentificationModel description.', max_length=256, null=True, validators=[autocli2.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='IdentificationModel graphical representation.', verbose_name='IdentificationModel ico')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is StatusModel deleted (Deleted StatusModel is reserved for backward compatibility).', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is StatusModel root (Root StatusModel cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is StatusModel active (Inactive StatusModel has limited functionality).', verbose_name='Active')),
                ('execution_protocol', models.IntegerField(choices=[(1, 'SSH'), (2, 'HTTP')], default=1, help_text='The network protocol that will be used to execute connection template (SSH / HTTP(S)).', verbose_name='Execution protocol')),
                ('ssh_type', models.IntegerField(choices=[(1, 'Command'), (2, 'template')], default=1, help_text='Type of SSH connection template (Command / template).', verbose_name='SSH execution type')),
                ('ssh_command', models.CharField(blank=True, help_text='The CLI command that will be executed on the remote host.', max_length=128, null=True, verbose_name='CLI command')),
                ('ssh_template', models.TextField(blank=True, help_text='SSh template will be used to create CLI command(s), which will be executed in the remote host to change configuration.', null=True, verbose_name='Template')),
                ('http_method', models.IntegerField(choices=[(1, 'GET'), (2, 'POST'), (3, 'PUT'), (4, 'DELETE')], default=1, help_text='Type of HTTP request method (GET, POST, PUT, DELETE).', verbose_name='HTTP(S) request method')),
                ('http_url', models.CharField(blank=True, help_text='HTTP(S) URL field used to generate API request.', max_length=128, null=True, verbose_name='HTTP(S) URL')),
                ('http_header', models.JSONField(blank=True, help_text='HTTP(S) heder field used to generate API request.', null=True, verbose_name='HTTP(S) heder')),
                ('http_params', models.JSONField(blank=True, help_text='HTTP(S) parameters field used to generate API request.', null=True, verbose_name='HTTP(S) parameters')),
                ('http_body', models.JSONField(blank=True, help_text='HTTP(S) body field used to generate API request.', null=True, verbose_name='HTTP(S) body')),
                ('sfm_expression', models.TextField(blank=True, help_text='FSM expression used to validate the output after the execution of the template.', null=True, verbose_name='SFM expression')),
                ('regex_expression', models.TextField(blank=True, help_text='Regex expression used to validate the output after the execution of the template.', null=True, verbose_name='Regex expression')),
                ('connection_template_groups', models.ManyToManyField(help_text='Connection template can be added to one or more connection template group(s). For the purpose of arranging templates in order.', to='connector.connectiongroup', verbose_name='Connection template group')),
                ('softwares', models.ManyToManyField(help_text='One or more software(s) can be added to the connection template. To associate the template with the appropriate software(s). Template execution will only be available to hosts belonging to the specified software.', to='inventory.software', verbose_name='Software')),
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
                ('created', models.DateTimeField(auto_now_add=True, help_text='DataTimeModel create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='DataTimeModel last update date.', verbose_name='Updated')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is StatusModel deleted (Deleted StatusModel is reserved for backward compatibility).', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is StatusModel root (Root StatusModel cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is StatusModel active (Inactive StatusModel has limited functionality).', verbose_name='Active')),
                ('keys', models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='Keys')),
                ('keys_regex', models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Xxx')),
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
                ('created', models.DateTimeField(auto_now_add=True, help_text='DataTimeModel create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='DataTimeModel last update date.', verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'IdentificationModel with this name already exists.'}, help_text='IdentificationModel name.', max_length=64, unique=True, validators=[autocli2.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=64, unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, default='IdentificationModel default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='IdentificationModel description.', max_length=256, null=True, validators=[autocli2.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='IdentificationModel graphical representation.', verbose_name='IdentificationModel ico')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is StatusModel deleted (Deleted StatusModel is reserved for backward compatibility).', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is StatusModel root (Root StatusModel cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is StatusModel active (Inactive StatusModel has limited functionality).', verbose_name='Active')),
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
                ('created', models.DateTimeField(auto_now_add=True, help_text='DataTimeModel create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='DataTimeModel last update date.', verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'IdentificationModel with this name already exists.'}, help_text='IdentificationModel name.', max_length=64, unique=True, validators=[autocli2.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='IdentificationModel name representation (Slug).', max_length=64, unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, default='IdentificationModel default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='IdentificationModel description.', max_length=256, null=True, validators=[autocli2.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='IdentificationModel graphical representation.', verbose_name='IdentificationModel ico')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is StatusModel deleted (Deleted StatusModel is reserved for backward compatibility).', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is StatusModel root (Root StatusModel cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is StatusModel active (Inactive StatusModel has limited functionality).', verbose_name='Active')),
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
                ('created', models.DateTimeField(auto_now_add=True, help_text='DataTimeModel create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='DataTimeModel last update date.', verbose_name='Updated')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is StatusModel deleted (Deleted StatusModel is reserved for backward compatibility).', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Is StatusModel root (Root StatusModel cannot be deleted or modify).', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Is StatusModel active (Inactive StatusModel has limited functionality).', verbose_name='Active')),
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
        migrations.AddField(
            model_name='datagrouptemplate',
            name='softwares',
            field=models.ManyToManyField(help_text='One or more software(s) can be added to the connection template. To associate the template with the appropriate software(s). Template execution will only be available to hosts belonging to the specified software.', to='inventory.software', verbose_name='Software'),
        ),
    ]
