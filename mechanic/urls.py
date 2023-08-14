from django.urls import path,include
from rest_framework import routers
from .api.viewsets import MechanicViewSet


router = routers.DefaultRouter()
router.register('',MechanicViewSet, basename='mechanic')

urlpatterns = [
    path('',include(router.urls))
]