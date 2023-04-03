# AutoCli2 - base integer model import:
from autocli2.base.constants.base.base_choices import BaseTextChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class DeviceTypeChoices(BaseTextChoices):

    # Choices values:
    DISCOVERY = 'discovery', 'Discovery'
    UNSUPPORTED = 'unsupported', 'Unsupported'
    CISCO_IOS = 'cisco_ios', 'Cisco IOS'
    CISCO_IOSXE = 'cisco_iosxe', 'Cisco IOS XE'
