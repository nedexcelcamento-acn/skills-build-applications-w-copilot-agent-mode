"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import os

# Dummy viewsets for demonstration (replace with actual viewsets if implemented)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class DummyViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'API endpoint works'})

router = routers.DefaultRouter()
router.register(r'users', DummyViewSet, basename='users')
router.register(r'teams', DummyViewSet, basename='teams')
router.register(r'activities', DummyViewSet, basename='activities')
router.register(r'leaderboard', DummyViewSet, basename='leaderboard')
router.register(r'workouts', DummyViewSet, basename='workouts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
