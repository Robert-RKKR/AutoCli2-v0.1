# Generated by Django 4.1.7 on 2023-04-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_globalsettings_ssh_repeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='ssh_invalid_responses',
            field=models.JSONField(default=['% Invalid input detected', 'syntax error, expecting', 'Error: Unrecognized command', '%Error', 'command not found', 'Syntax Error: unexpected argument', '% Unrecognized command found at', 'invalid input detected', 'cdp is not enabled', 'incomplete command', 'no spanning tree instance exists', 'lldp is not enabled', 'snmp agent not enabled'], help_text='List of strings that contain invalid host responses. For example, the Cisco IOS system returns output such as "invalid input detected" in the case of an unsupported command, or "cdp is not enabled" in the case of an disabled function, in this example CDP.', verbose_name='SSH invalid responses'),
        ),
    ]
