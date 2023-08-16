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
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MjE4NjYxNSwiaWF0IjoxNjkyMTAwMjE1LCJqdGkiOiIwNTUxMjE0MmE5NTU0MzliOGM1MTQ2MGZlMTgwMjhlYiIsInVzZXJfaWQiOjN9.QUFwvlyfWs8lmEoCGwYX0DlraIqPVkKgs-ko0pLVrkA",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMTAwNTE1LCJpYXQiOjE2OTIxMDAyMTUsImp0aSI6IjY4YWIzNWZlYzMzNzQyNTM4MTZhOTc2ODliOTdlODE4IiwidXNlcl9pZCI6M30.-9KFimCDBJaLPhtikvGcJu8k17okrAC2mRcSvyPZDJ8"
# }