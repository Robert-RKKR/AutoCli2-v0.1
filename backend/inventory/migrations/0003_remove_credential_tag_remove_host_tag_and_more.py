# Generated by Django 4.1.7 on 2023-03-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credential',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='host',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='region',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='site',
            name='tag',
        ),
        migrations.AddField(
            model_name='credential',
            name='tag',
            field=models.ManyToManyField(help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='host',
            name='tag',
            field=models.ManyToManyField(help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='platform',
            name='tag',
            field=models.ManyToManyField(help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='region',
            name='tag',
            field=models.ManyToManyField(help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='site',
            name='tag',
            field=models.ManyToManyField(help_text='Related tag.', to='inventory.tag', verbose_name='Tag'),
        ),
    ]
