"""
URL configuration for swimmingplaces project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from src import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LocationViewSet.as_view({'get': 'list'}), name='locations_template'),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('statistics/', views.LocationViewSet.as_view({'get': 'statistics'}), name='statistics'),
]