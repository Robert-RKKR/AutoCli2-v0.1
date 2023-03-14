# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from .view_sets.root import InventoryRootView

# AutoCli2 - simple view set import:
from .view_sets.host import HostSimpleView

# AutoCli2 - standard view set import:
from .view_sets.host import HostView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Root api view route registration:
router.APIRootView = InventoryRootView

# Standard view route registration:
router.register(r'host', HostView, basename='host')

# Simple view route registration:
# router.register(r'simple_host', HostSimpleView, basename='simple_host')

# Add urlpatterns:
urlpatterns = router.urls
