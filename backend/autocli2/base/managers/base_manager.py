# Django - model import:
from django.db.models import Manager


# Base manager class:
class BaseManager(Manager):

    def get_queryset(self):
        return super(
            BaseManager, self
        ).get_queryset().filter(is_deleted=False)

    def get_by_natural_key(self, name):
        return self.get(name=name)
