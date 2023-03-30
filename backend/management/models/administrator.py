# Django - model import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - abstract user import:
from django.contrib.auth.models import AbstractUser

# AutoCli2 - administrator manager import:
from management.managers.administrator import AdministratorManager


# Administrator model class:
class Administrator(AbstractUser):

    class Meta:
        
        # Model name values:
        verbose_name = _('Administrator')
        verbose_name_plural = _('Administrators')

    # Model objects manager:
    objects = AdministratorManager()

    # Relations with other classes:
    api_token = models.CharField(
        verbose_name=_('Token'),
        help_text=_('Token that will be used during API request.'),
        max_length=128,
        null=True,
        blank=True,
    )
