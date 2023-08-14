from django.urls import path, include
from rest_framework import routers
from .viewsets import MakePairViewSets


router = routers.DefaultRouter()
router.register('',MakePairViewSets, basename='make_pair')

urlpatterns = [
    path('',include(router.urls)),
]