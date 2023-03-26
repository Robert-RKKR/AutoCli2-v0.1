# Generated by Django 4.1.7 on 2023-03-26 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='administrator',
            field=models.ForeignKey(blank=True, help_text='Administrator responsible for provided AdministratorModel.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Administrator'),
        ),
        migrations.AddField(
            model_name='credential',
            name='tag',
            field=models.ForeignKey(blank=True, help_text='Related tag.', null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.tag', verbose_name='Tag'),
        ),
    ]
