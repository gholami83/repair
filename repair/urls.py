from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authuser/',include('authuser.urls')),
    path('driver/',include('driver.urls')),
    path('mechanic/',include('mechanic.urls')),
    path('pair/',include('pair.urls',namespace='pair')),
    path('technic-assist/',include('technical_assistant.urls')),
    path('api/',include('gettoken.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
