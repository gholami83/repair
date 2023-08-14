from django.urls import path, include
from rest_framework import routers
from .viewsets import MakePairViewSets,UpdatePair


router = routers.DefaultRouter()
router.register('',MakePairViewSets, basename='make_pair')
router.register('update-pair',viewset=UpdatePair,basename='updatepair')

urlpatterns = [
    path('',include(router.urls)),
]