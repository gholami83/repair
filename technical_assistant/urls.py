from django.urls import path,include
from rest_framework import routers
from api.viewsets import assistantviewsets



router = routers.DefaultRouter()
router.register('',viewset=assistantviewsets, basename='assistant')

urlpatterns = [
    path('',include(router.urls)),
]

