# Generated by Django 4.1.7 on 2023-03-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0014_connectiontemplate_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectiontemplate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='connectiontemplate',
            name='execution_protocol',
            field=models.IntegerField(choices=[(None, 'Empty'), ('HTTP', 'HTTP(S)'), ('SSH', 'SSH'), ('DS', 'Discovery')], default=1, help_text='The network protocol that will be used to execute connection template (SSH / HTTP(S)).', verbose_name='Execution protocol'),
        ),
        migrations.AlterField(
            model_name='connectiontemplate',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='connectiontemplate',
            name='is_root',
            field=models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root'),
        ),
        migrations.AlterField(
            model_name='connectiontemplate',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='datagrouptemplate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='datagrouptemplate',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='datagrouptemplate',
            name='is_root',
            field=models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root'),
        ),
        migrations.AlterField(
            model_name='datagrouptemplate',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='datatemplate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='datatemplate',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='datatemplate',
            name='is_root',
            field=models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root'),
        ),
        migrations.AlterField(
            model_name='datatemplate',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='modelgrouptemplate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='modelgrouptemplate',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='modelgrouptemplate',
            name='is_root',
            field=models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root'),
        ),
        migrations.AlterField(
            model_name='modelgrouptemplate',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='modeltemplate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Base model create date.', verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='modeltemplate',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is Base model active (Inactive Base model has limited functionality).', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='modeltemplate',
            name='is_root',
            field=models.BooleanField(default=False, help_text='Is Base model root (Root Base model cannot be deleted or modify).', verbose_name='Root'),
        ),
        migrations.AlterField(
            model_name='modeltemplate',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Base model last update date.', verbose_name='Updated'),
        ),
    ]