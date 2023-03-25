# Django - application import:
from django.apps import AppConfig

# Django - signals import:
from django.db.models.signals import post_migrate


# App class:
class AppInitiatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_initiator'

    def ready(self):

        # AutoCli2 - inventory model import:
        from inventory.models.credentials import Credential
        from inventory.models.platform import Platform

        # AutoCli2 - executor model import:
        from management.models.administrator import Administrator

        def create_initial_data(sender, **kwargs):

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

            # Create base administrator objects if not exists:
            Administrator.objects.get_or_create(
                username = 'admin-1',
                email = 'admin@autocli2.com',
                is_staff = True,
                is_active = True,
                is_superuser = True,
                password = 'pbkdf2_sha256$390000$JCynP2LLbnqlZIUz0edcSp$r0Ke5G42LaunhJfGbT5Uk1CAt42RA12qeYSUHaDepH0='
            )

        # connect the function to the post_migrate signal
        post_migrate.connect(create_initial_data, sender=self)
