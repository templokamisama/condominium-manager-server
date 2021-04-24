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
from django.urls import re_path
from user.views import UserViewSet


urlpatterns = [
    re_path(r'^sign-up/?$', UserViewSet.as_view({'post': 'sign_up'}), name='sign_up'),
    re_path(r'^sign-in/?$', UserViewSet.as_view({'post': 'sign_in'}), name='sign_in'),
]
