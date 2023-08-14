from django.urls import path, include
from rest_framework import routers
from .viewsets import MakePairViewSets,CostPairViewSets,PayPairViewSets


router = routers.DefaultRouter()
router.register('list',MakePairViewSets, basename='make_pair')
router.register('cost',CostPairViewSets, basename='paircost')
router.register('pay',PayPairViewSets, basename='paircost')



urlpatterns = [
    path('',include(router.urls)),
]