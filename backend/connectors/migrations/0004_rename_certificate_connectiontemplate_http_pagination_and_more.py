# Generated by Django 4.1.4 on 2023-02-08 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('connectors', '0003_connectiongroup_connectionsshtemplate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectiontemplate',
            old_name='certificate',
            new_name='http_pagination',
        ),
        migrations.RenameField(
            model_name='connectiontemplate',
            old_name='https_url',
            new_name='http_url',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='execution_method',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='https_body',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='https_header',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='https_method',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='https_pagination',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='https_pagination_path',
        ),
        migrations.RemoveField(
            model_name='connectiontemplate',
            name='https_params',
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='execution_protocol',
            field=models.IntegerField(choices=[(1, 'SSH'), (2, 'HTTP')], default=1, help_text='Network protocol used to execute the connection template (SSH / HTTP).', verbose_name='Execution protocol'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='http_body',
            field=models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='HTTP body'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='http_header',
            field=models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='HTTP heder'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='http_method',
            field=models.IntegerField(choices=[(1, 'GET'), (2, 'POST'), (3, 'PUT'), (4, 'DELETE')], default=1, help_text='Xx (HTTP request methods).', verbose_name='HTTP method'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='http_pagination_path',
            field=models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='HTTP body'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='http_params',
            field=models.JSONField(blank=True, help_text='Xxx.', null=True, verbose_name='HTTP parameters'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='platform',
            field=models.ForeignKey(blank=True, help_text='Platform.', null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.platform', verbose_name='Platform'),
        ),
    ]
