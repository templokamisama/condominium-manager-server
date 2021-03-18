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
from reservation.views import ProprietorViewSet, StructureViewSet


urlpatterns = [
    re_path(r'^proprietor/?$', ProprietorViewSet.as_view({'get': 'list'}), name='list'),
    re_path(r'^proprietor/?$', ProprietorViewSet.as_view({'post': 'post'}), name='post'),
    re_path(r'^structure/?$', StructureViewSet.as_view({'get': 'list_structures'}), name='list_structures'),
    re_path(r'^structure/delete/(?P<id>\d+)/?$', StructureViewSet.as_view({'delete': 'delete_structure'}), name='delete_structure'),
    re_path(r'^structure/create?$', StructureViewSet.as_view({'post': 'create_structure'}), name='create_structure'),
    re_path(r'^structure/(?P<id>\d+)/?$', StructureViewSet.as_view({'patch': 'edit_structure'}), name='edit_structure'),
]
