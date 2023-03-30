# Django - import:
from django.utils.deconstruct import deconstructible
from django.core import validators

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Validators classes:
@deconstructible
class CodeValueValidator(validators.RegexValidator):
    regex = r'^[A-Z,a-z]{2,8}$'
    message = _('The object code must contain 2 to 8 letters.')
    flags = 0
