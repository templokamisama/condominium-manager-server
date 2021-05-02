"""condominium_manager_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.exceptions import MethodNotAllowed

SchemaView = get_schema_view(
    openapi.Info(
        title='Meu Condominium API',
        default_version='v1',
        description='',
        terms_of_service=''
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include(('reservation.urls', 'reservation'), namespace='reservation')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
]


def swagger_method_dispatch(**table):
    """
    Swagger dispatcher
    """

    def invalid_method(request):
        return MethodNotAllowed(request.method)

    def dispatch(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)

    return dispatch


# Enable docs
if settings.DEBUG:
    urlpatterns = [
        path(
            "docs/",
            swagger_method_dispatch(GET=SchemaView.with_ui("swagger", cache_timeout=None)),
            name="docs",
        )
    ] + urlpatterns

    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
