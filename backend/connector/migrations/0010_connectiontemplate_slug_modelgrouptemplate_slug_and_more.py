# Generated by Django 4.1.7 on 2023-03-19 12:44

import connector.validators.connection_template_validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0009_remove_connectiontemplate_sfm_expression'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectiontemplate',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelgrouptemplate',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modeltemplate',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, help_text='IdentificationModel name representation (Slug).', max_length=512, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='connectiontemplate',
            name='regex_expression',
            field=models.TextField(blank=True, help_text='Regex expression used to validate the output after the execution of the template.', null=True, validators=[connector.validators.connection_template_validators.regex_validator], verbose_name='Regex expression'),
        ),
        migrations.AlterField(
            model_name='connectiontemplate',
            name='response_type',
            field=models.IntegerField(choices=[(1, '----'), (2, 'List'), (3, 'Dict'), (4, 'String')], default=1, help_text='Xxx.', verbose_name='Type of response'),
        ),
    ]
