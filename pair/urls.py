from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from .api.viewsets import MakePairViewSets,CostPairViewSets,PayPairViewSets


app_name = 'pair'

router = routers.DefaultRouter()
router.register('list',MakePairViewSets, basename='make_pair')
router.register('cost',CostPairViewSets, basename='paircost')
router.register('pay',PayPairViewSets, basename='paircost')

    
urlpatterns = [
    path('',include(router.urls),name='router-urls'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]