# Generated by Django 4.1.7 on 2023-03-26 20:43

import autocli2.base.validators.base_validator
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import management.managers.administrator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSetting',
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
                ('is_current', models.BooleanField(default=True, help_text='Xxx', verbose_name='Current global settings')),
                ('notification_level', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=4, help_text='The level of severity of the performed action.', verbose_name='Notification severity level')),
                ('logger_level', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=1, help_text='The level of severity of the performed action.', verbose_name='Logger severity level')),
                ('default_user', models.CharField(default='admin', help_text='Xxx.', max_length=128, verbose_name='Default username')),
                ('default_password', models.CharField(default='!Cisco123', help_text='Xxx.', max_length=128, verbose_name='Default password')),
                ('http_timeout', models.IntegerField(default=10, help_text='Xxx.', verbose_name='HTTP session timeout')),
                ('ssh_timeout', models.IntegerField(default=10, help_text='Xxx.', verbose_name='SSH session timeout')),
            ],
            options={
                'verbose_name': 'Global setting',
                'verbose_name_plural': 'Global settings',
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('api_token', models.CharField(help_text='Token that will be used during API request.', max_length=128, verbose_name='Token')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
            },
            managers=[
                ('objects', management.managers.administrator.AdministratorManager()),
            ],
        ),
    ]