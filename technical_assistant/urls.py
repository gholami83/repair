from django.urls import path,include
from rest_framework import routers
from .api.viewsets import AssistantViewSet


router = routers.DefaultRouter()
router.register('',viewset=AssistantViewSet, basename='assistant')


urlpatterns = [
    path('',include(router.urls)),
]

