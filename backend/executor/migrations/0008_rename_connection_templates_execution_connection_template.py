# Generated by Django 4.1.4 on 2023-03-05 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0007_rename_hosts_execution_host'),
    ]

    operations = [
        migrations.RenameField(
            model_name='execution',
            old_name='connection_templates',
            new_name='connection_template',
        ),
    ]
