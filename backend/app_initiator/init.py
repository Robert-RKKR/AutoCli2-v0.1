# Init application DB:
def init_app_db():

    # AutoCli2 - inventory model import:
    from inventory.models.credentials import Credential
    from inventory.models.platform import Platform

    # Create base Credential object if not exist:
    Credential.objects.get_or_create(
        name = 'Default credentials',
        description = 'Default AutoCli 2 credentials.',
        is_global = True,
        username = 'admin',
        password = '!Cisco@12345'
    )

    # Create base Platform objects if not exists:
    Platform.objects.get_or_create(
        is_root = True,
        name = 'Discover',
        description = 'Discover host platform.'
    )
