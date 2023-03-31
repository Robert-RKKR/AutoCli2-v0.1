# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from management.api.view_sets.root import ManagementRootView

# AutoCli2 - standard view set import:
from management.api.view_sets.global_settings import GlobalSettingsView
from management.api.view_sets.administrator import AdministratorView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-management'

# Root api view route registration:
router.APIRootView = ManagementRootView

# Standard view route registration:
router.register(r'global-settings', GlobalSettingsView, basename='global-settings')
router.register(r'administrator', AdministratorView, basename='administrator')

# Add urlpatterns:
urlpatterns = router.urls
