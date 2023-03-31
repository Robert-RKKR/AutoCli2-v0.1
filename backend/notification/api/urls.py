# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from notification.api.view_sets.root import NotificationRootView

# AutoCli2 - standard view set import:
from notification.api.view_sets.notification import NotificationView
from notification.api.view_sets.change_log import ChangeLogView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-notification'

# Root api view route registration:
router.APIRootView = NotificationRootView

# Standard view route registration:
router.register(r'notification', NotificationView, basename='notification')
router.register(r'change-log', ChangeLogView, basename='change-log')

# Add urlpatterns:
urlpatterns = router.urls
