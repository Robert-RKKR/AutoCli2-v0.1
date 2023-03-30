# Django - choices model import:
from django.db.models import TextChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ColorChoices(TextChoices):

    # Choices values:
    DARK_RED = 'aa1409', _('Dark red')
    RED = 'f44336', _('Red')
    PINK = 'e91e63', _('Pink')
    ROSE = 'ffe4e1', _('Rose')
    FUCHSIA = 'ff66ff', _('Fuchsia')
    PURPLE = '9c27b0', _('Purple')
    DARK_PURPLE = '673ab7', _('Dark purple')
    INDIGO = '3f51b5', _('Indigo')
    BLUE = '2196f3', _('Blue')
    LIGHT_BLUE = '03a9f4', _('Light blue')
    CYAN = '00bcd4', _('Cyan')
    TEAL = '009688', _('Teal')
    AQUA = '00ffff', _('Aqua')
    DARK_GREEN = '2f6a31', _('Dark green')
    GREEN = '4caf50', _('Green')
    LIGHT_GREEN = '8bc34a', _('Light green')
    LIME = 'cddc39', _('Lime')
    YELLOW = 'ffeb3b', _('Yellow')
    AMBER = 'ffc107', _('Amber')
    ORANGE = 'ff9800', _('Orange')
    DARK_ORANGE = 'ff5722', _('Dark orange')
    BROWN = '795548', _('Brown')
    LIGHT_GREY = 'c0c0c0', _('Light grey')
    GREY = '9e9e9e', _('Grey')
    DARK_GREY = '607d8b', _('Dark grey')
    BLACK = '111111', _('Black')
    WHITE = 'ffffff', _('White')
