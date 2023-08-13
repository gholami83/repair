from django.urls import path,include
from rest_framework import routers
from .viewsets import DriverViewSets


router = routers.DefaultRouter()
router.register('',viewset=DriverViewSets,basename='driver')

urlpatterns = [
    path('',include(router.urls)),
]