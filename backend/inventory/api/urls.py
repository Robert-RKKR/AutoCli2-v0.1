# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from inventory.api.view_sets.root import InventoryRootView

# AutoCli2 - simple view set import:
from inventory.api.view_sets.credentials import CredentialFullView
from inventory.api.view_sets.host import HostFullView
from inventory.api.view_sets.site import SiteFullView

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
router.register(r'full_credential', CredentialFullView, basename='full_credential')
router.register(r'full_host', HostFullView, basename='full_host')
router.register(r'full_site', SiteFullView, basename='full_site')

# Standard view route registration:
router.register(r'credential', CredentialView, basename='credential')
router.register(r'platform', PlatformView, basename='platform')
router.register(r'region', RegionView, basename='region')
router.register(r'host', HostView, basename='host')
router.register(r'site', SiteView, basename='site')

# Add urlpatterns:
urlpatterns = router.urls
