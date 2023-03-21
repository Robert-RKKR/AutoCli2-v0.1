# Django - import:
from django.utils.deconstruct import deconstructible
from django.core import validators


# Validators classes:
@deconstructible
class CodeValueValidator(validators.RegexValidator):
    regex = r'^[A-Z,a-z]{2,8}$'
    message = 'The object code must contain 2 to 8 letters.'
    flags = 0
