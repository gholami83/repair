from django.urls import path,include
from rest_framework import routers
from . import viewsets


router = routers.DefaultRouter()
router.register('',viewsets.UserRegisterViewSets,basename='authuser')

urlpatterns = [
    path('',include(router.urls)),
]