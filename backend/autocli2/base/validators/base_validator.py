# Django - import:
from django.utils.deconstruct import deconstructible
from django.core import validators


# Validators classes:
@deconstructible
class NameValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_. ]{4,64}$'
    message = 'The object hostname must contain 4 to 64 digits, letters and special characters -, _, . or spaces.'
    flags = 0


@deconstructible
class DescriptionValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_." ]{8,256}$'
    message = 'Description must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'
    flags = 0
