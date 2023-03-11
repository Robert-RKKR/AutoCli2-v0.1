# Generated by Django 4.1.4 on 2023-03-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_host_credential_alter_host_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='certificate_check',
            field=models.BooleanField(default=True, help_text='If enabled, attempts to validate host certificate. If disabled, ignores certificate validation process.', verbose_name='Certificate check'),
        ),
    ]