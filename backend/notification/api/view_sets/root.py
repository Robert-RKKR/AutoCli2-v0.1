# Rest framework - routers import:
from rest_framework.routers import APIRootView


# Root API view:
class NotificationRootView(APIRootView):
    """
    Notification API root view.
    """
    
    def get_view_name(self):
        return 'api-notification'
