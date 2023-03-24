# Generated by Django 4.1.7 on 2023-03-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_host_data_collection_protocol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='data_collection_protocol',
            field=models.IntegerField(choices=[(1, 'SSH'), (2, 'HTTP(S)'), (3, 'Discovery')], default=1, help_text='The network protocol that will be used to execute connection template (SSH / HTTP(S)).', verbose_name='Data collection protocol'),
        ),
    ]
