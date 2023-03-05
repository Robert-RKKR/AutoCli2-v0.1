# Generated by Django 4.1.4 on 2023-03-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0010_remove_execution_result_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='execution',
            name='connection_template_representation',
            field=models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Connection template representation'),
        ),
        migrations.AddField(
            model_name='execution',
            name='credential_representation',
            field=models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Credential representation'),
        ),
        migrations.AddField(
            model_name='execution',
            name='host_representation',
            field=models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Host representation'),
        ),
    ]
