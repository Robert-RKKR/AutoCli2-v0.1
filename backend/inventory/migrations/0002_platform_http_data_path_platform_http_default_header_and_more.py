# Generated by Django 4.1.7 on 2023-04-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='http_data_path',
            field=models.JSONField(blank=True, help_text='The data path value is used to collect useful data included in the HTTP(S) response.', null=True, verbose_name='HTTP(S) data path'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_default_header',
            field=models.JSONField(blank=True, help_text='Default heder used during HTTP(S) requests.', null=True, verbose_name='HTTP(S) default heder'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_default_params',
            field=models.JSONField(blank=True, help_text='Default parameters used during HTTP(S) requests.', null=True, verbose_name='HTTP(S) default parameters'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_next_page_code_path',
            field=models.JSONField(blank=True, help_text='The next page path value is used by the connection template when the HTTP(S) request returns a response, that is divided into many pages (paginated response). In this case next page path value is used to retrieve the pagination code required to prepare the next HTTP(S) request for other pages (The value will only be used if the pagination field is enabled).', null=True, verbose_name='HTTP(S) next page code path'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_next_page_link_path',
            field=models.JSONField(blank=True, help_text='The next page path value is used by the connection template when the HTTP(S) request returns a response that is divided into many pages (paginated response). In this case, the next page path value is used to retrieve the pagination URL link used in the next HTTP(S) request for other pages (The value will only be used if the pagination field is enabled).', null=True, verbose_name='HTTP(S) next page link path'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_pagination',
            field=models.BooleanField(default=False, help_text='When the pagination value is active, the HTTP(S) request will be repeated to collect all objects from all paginated pages.', verbose_name='HTTP(S) pagination'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_pagination_param_key',
            field=models.CharField(blank=True, help_text='Information collected based on the next page code path value is added to the URL with a specific code. This code should be provided as a pagination param key value. For example, the value "cursor" will be added to the URL in the form "?cursor={{next page code}}" (The value will only be used if the pagination field is enabled).', max_length=128, null=True, verbose_name='HTTP(S) pagination param key'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_token_heder_key',
            field=models.CharField(blank=True, help_text='When authenticating an HTTP(S) connection using an API token, the token key value is defined in the HTTP(S) request header . In the example "Authorization=API_Token {{key}}", the token header key value is Authorization.', max_length=128, null=True, verbose_name='API token heder key'),
        ),
        migrations.AddField(
            model_name='platform',
            name='http_token_heder_value',
            field=models.CharField(blank=True, help_text='When authenticating an HTTP(S) connection using an API token, the token value is defined in the HTTP(S) request header . In the example "Authorization=API_Token {{key}}", the token header value is API_Token.', max_length=128, null=True, verbose_name='API token heder value'),
        ),
        migrations.AddField(
            model_name='platform',
            name='is_http_supported',
            field=models.BooleanField(default=False, help_text='Is HTTP(S) protocol supported by platform.', verbose_name='Is HTTP(S) supported'),
        ),
        migrations.AddField(
            model_name='platform',
            name='is_ssh_supported',
            field=models.BooleanField(default=False, help_text='Is SSH protocol supported by platform.', verbose_name='Is SSH supported'),
        ),
        migrations.AddField(
            model_name='platform',
            name='ssh_device_type',
            field=models.CharField(choices=[('discovery', 'Discovery'), ('unsupported', 'Unsupported'), ('cisco_ios', 'Cisco IOS'), ('cisco_iosxe', 'Cisco IOS XE')], default='discovery', help_text='Netmiko device type (SSH only).', max_length=32, verbose_name='Netmiko device type'),
        ),
        migrations.AddField(
            model_name='platform',
            name='ssh_invalid_responses',
            field=models.JSONField(blank=True, help_text='List of strings that contain invalid host responses. For example, the Cisco IOS system returns output such as "invalid input detected" in the case of an unsupported command, or "cdp is not enabled" in the case of an unenabled function, in this example CDP.', null=True, verbose_name='SSH invalid responses'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='host',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='region',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='site',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='platform',
            unique_together={('is_ssh_supported', 'ssh_device_type')},
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_data_path',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_default_header',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_default_params',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_next_page_code_path',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_next_page_link_path',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_pagination',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_pagination_param_key',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_token_heder_key',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_token_heder_value',
        ),
    ]
