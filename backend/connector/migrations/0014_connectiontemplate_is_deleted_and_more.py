# Generated by Django 4.1.7 on 2023-03-22 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0013_alter_connectiontemplate_execution_protocol_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectiontemplate',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted'),
        ),
        migrations.AddField(
            model_name='datagrouptemplate',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted'),
        ),
        migrations.AddField(
            model_name='datatemplate',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted'),
        ),
        migrations.AddField(
            model_name='modelgrouptemplate',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted'),
        ),
        migrations.AddField(
            model_name='modeltemplate',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Is Base model object deleted.', verbose_name='Deleted'),
        ),
    ]
