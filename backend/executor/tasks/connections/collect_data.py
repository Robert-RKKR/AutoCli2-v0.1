# Python - library import:
import threading

# Django - translation model import:
from django.utils.translation import gettext as _

# AutoCli2 - connection class import:
from executor.tasks.connections.connection import ConnectionTask


# Test taks class:
class CollectHostData(ConnectionTask):
    """
    Abstract task responsible for host data collection.
    """

    
