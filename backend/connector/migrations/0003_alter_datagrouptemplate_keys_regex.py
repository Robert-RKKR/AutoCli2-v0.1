# Generated by Django 4.1.4 on 2023-03-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0002_remove_connectiontemplate_connection_template_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datagrouptemplate',
            name='keys_regex',
            field=models.CharField(blank=True, help_text='Xxx.', max_length=128, null=True, verbose_name='Keys REGEX'),
        ),
    ]
