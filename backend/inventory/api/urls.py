# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from inventory.api.view_sets.root import InventoryRootView

# AutoCli2 - simple view set import:
from inventory.api.view_sets.credentials import CredentialSimpleView
from inventory.api.view_sets.platform import PlatformSimpleView
from inventory.api.view_sets.region import RegionSimpleView
from inventory.api.view_sets.host import HostSimpleView
from inventory.api.view_sets.site import SiteSimpleView

# AutoCli2 - standard view set import:
from inventory.api.view_sets.credentials import CredentialView
from inventory.api.view_sets.platform import PlatformView
from inventory.api.view_sets.region import RegionView
from inventory.api.view_sets.host import HostView
from inventory.api.view_sets.site import SiteView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Root api view route registration:
router.APIRootView = InventoryRootView

# Simple view route registration:
router.register(r'simple_credential', CredentialSimpleView, basename='simple_credential')
router.register(r'simple_platform', PlatformSimpleView, basename='simple_platform')
router.register(r'simple_region', RegionSimpleView, basename='simple_region')
router.register(r'simple_host', HostSimpleView, basename='simple_host')
router.register(r'simple_site', SiteSimpleView, basename='simple_site')

# Standard view route registration:
router.register(r'credential', CredentialView, basename='credential')
router.register(r'platform', PlatformView, basename='platform')
router.register(r'region', RegionView, basename='region')
router.register(r'host', HostView, basename='host')
router.register(r'site', SiteView, basename='site')

# Add urlpatterns:
urlpatterns = router.urls
