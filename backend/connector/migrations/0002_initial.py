# Generated by Django 4.1.7 on 2023-03-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('connector', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datagrouptemplate',
            name='platform',
            field=models.ManyToManyField(help_text='One or more software(s) can be added to the connection template. To associate the template with the appropriate software(s). Template execution will only be available to hosts belonging to the specified software.', to='inventory.platform', verbose_name='Software'),
        ),
        migrations.AddField(
            model_name='connectiontemplate',
            name='platforms',
            field=models.ManyToManyField(help_text='One or more platform(s) can be added to the connection template. To associate the template with the appropriate platform(s). Template execution will only be available to hosts belonging to the specified platform.', to='inventory.platform', verbose_name='Platform'),
        ),
    ]