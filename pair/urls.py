from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from .api.viewsets import MakePairViewSets,CostPairViewSets,PayPairViewSets


app_name = 'pair'
router = routers.DefaultRouter()
router.register('list',MakePairViewSets, basename='make_pair')
router.register('cost',CostPairViewSets, basename='costs')
router.register('pay',PayPairViewSets, basename='pays')

    
urlpatterns = [
    path('',include(router.urls),name='router-urls'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]