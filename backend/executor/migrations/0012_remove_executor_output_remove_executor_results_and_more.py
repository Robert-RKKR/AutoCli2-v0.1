# Generated by Django 4.1.4 on 2023-03-07 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0011_execution_connection_template_representation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executor',
            name='output',
        ),
        migrations.RemoveField(
            model_name='executor',
            name='results',
        ),
        migrations.RemoveField(
            model_name='executor',
            name='status',
        ),
    ]