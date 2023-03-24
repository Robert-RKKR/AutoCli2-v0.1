# Generated by Django 4.1.7 on 2023-03-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_alter_credential_created_alter_credential_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='data_collection_protocol',
            field=models.CharField(choices=[(None, 'Empty'), ('http', 'HTTP(S)'), ('ssh', 'SSH'), ('dsc', 'Discovery')], default='HTTP', help_text='The network protocol that will be used to execute connection template (SSH / HTTP(S)).', max_length=4, verbose_name='Data collection protocol'),
        ),
    ]