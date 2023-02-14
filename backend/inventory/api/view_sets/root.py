# Rest framework import:
from rest_framework.routers import APIRootView


# Root API view:
class InventoryRootView(APIRootView):
    """
    Inventory API root view.
    """
    def get_view_name(self):
        return 'api-inventory'
