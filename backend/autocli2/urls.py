# Django - url import:
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path

# Rest framework - views import:
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions

# Main API view import:
from autocli2.base.api.base_api_root_view import APIRootView

# DRF yasg - views import:
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Register Swagger view:
schema_view = get_schema_view(
    openapi.Info(
        title="AutoCLI 2 API documentation",
        default_version='v0.1',
        description="Welcome to the AutoCLI 2 - network automation tool API",
        contact=openapi.Contact(email="robert.kucharski.rkkr@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URLs registration:
urlpatterns = [
    # Django admin registration:
    path('admin/', admin.site.urls),

    # Main API views registration:
    path('api/', APIRootView.as_view(), name='api-root'),
    path('api-admin/token-auth/', obtain_auth_token),

    # API documentation views registration:
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api-admin/doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api-admin/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    # Test view registration:
    path('test/', include('a_test.urls')),

    # Network API view registration:
    path('api-inventory/', include('inventory.api.urls')),

    # API taks views:
    path('api-task/', include('executor.api.urls')),
]
