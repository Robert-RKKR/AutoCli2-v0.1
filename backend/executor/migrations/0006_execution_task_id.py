# Generated by Django 4.1.4 on 2023-03-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0005_remove_executor_execution_protocol'),
    ]

    operations = [
        migrations.AddField(
            model_name='execution',
            name='task_id',
            field=models.CharField(blank=True, help_text='ID of the associated task.', max_length=64, null=True, verbose_name='Task ID'),
        ),
    ]
