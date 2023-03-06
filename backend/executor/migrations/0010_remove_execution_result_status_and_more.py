# Generated by Django 4.1.4 on 2023-03-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0009_execution_ssh_response_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='execution',
            name='result_status',
        ),
        migrations.AddField(
            model_name='execution',
            name='execution_status',
            field=models.BooleanField(default=False, help_text='A positive result means that the command output was successfully received and processed.', verbose_name='Execution status'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='ssh_processed_data',
            field=models.JSONField(blank=True, help_text='CLI command FSM process data.', null=True, verbose_name='SSH command processed data'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='ssh_processed_data_status',
            field=models.BooleanField(default=False, help_text='A positive result means that the process of processing the data was completed successfully.', verbose_name='SSH processed data status'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='ssh_raw_data',
            field=models.TextField(blank=True, help_text='CLI command raw data output.', null=True, verbose_name='SSH command raw data'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='ssh_raw_data_status',
            field=models.BooleanField(default=False, help_text='A positive result means that the raw data collection process has been successfully completed.', verbose_name='SSH raw data status'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='ssh_response_status',
            field=models.BooleanField(default=False, help_text='Xxx.', verbose_name='SSH response status'),
        ),
    ]