# Generated by Django 4.1.7 on 2023-03-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0015_alter_connectiontemplate_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectiontemplate',
            name='execution_protocol',
            field=models.IntegerField(choices=[(None, 'Empty'), ('http', 'HTTP(S)'), ('ssh', 'SSH'), ('dsc', 'Discovery')], default=1, help_text='The network protocol that will be used to execute connection template (SSH / HTTP(S)).', verbose_name='Execution protocol'),
        ),
    ]
