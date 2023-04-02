# Django - signals import:
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Rest framework - token import:
from rest_framework.authtoken.models import Token

# Signal function:
@receiver(post_migrate)
def my_callback(sender, **kwargs):

    # AutoCli2 - inventory model import:
    from inventory.models.credentials import Credential
    from inventory.models.platform import Platform

    # Django - user model import:
    from django.contrib.auth.models import User

    # Create base credential object if not exist:
    Credential.objects.get_or_create(
        name = 'Default credentials',
        description = 'Default AutoCli 2 credentials.',
        is_global = True,
        username = 'admin',
        password = '!Cisco@12345'
    )

    # Create base platform objects if not exists:
    Platform.objects.get_or_create(
        is_root = True,
        name = 'Discover',
        description = 'Discover host platform.'
    )
    
    try: # Try to create base administrator objects if not exists:
        user = User.objects.get_or_create(
            username = 'admin',
            email = 'admin@autocli2.com',
            is_staff = True,
            is_active = True,
            is_superuser = True,
            password = 'pbkdf2_sha256$390000$JCynP2LLbnqlZIUz0edcSp$r0Ke5G42LaunhJfGbT5Uk1CAt42RA12qeYSUHaDepH0='
        )
        # Create an authentication token for the user
        token = Token.objects.create(user=user)
        print('\n\n\n======> ', token)
    except:
        pass
