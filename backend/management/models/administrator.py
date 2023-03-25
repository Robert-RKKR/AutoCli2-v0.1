# Django - model import:
from django.db import models

# Django - abstract user import:
from django.contrib.auth.models import AbstractUser

# AutoCli2 - administrator manager import:
from management.managers.administrator import AdministratorManager


# Administrator model class:
class Administrator(AbstractUser):

    class Meta:
        
        # Model name values:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

    # Model objects manager:
    objects = AdministratorManager()

    # Relations with other classes:
    api_token = models.CharField(
        verbose_name='Token',
        help_text='Token that will be used during API request.',
        max_length=128,
    )
