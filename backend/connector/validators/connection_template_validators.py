# Python regex import:
import re

# Django - import:
from django.core.exceptions import ValidationError


# Validators:
def regex_validator(value):
    pattern = rf'{value}'
    try:
        re.compile(pattern)
    except Exception as error:
        raise ValidationError(
            f'Regex validation error: {error}')
