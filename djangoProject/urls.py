from django.contrib import admin
from django.urls import path, include
from myapp import urls as myapp_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

swagger_urlpatterns = [
    path('doc/schema', SpectacularAPIView.as_view(), name='schema'),
    path('doc/schema/swagger', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('doc/schema/redoc/', SpectacularRedocView.as_view(), name='redoc' )
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(swagger_urlpatterns)),
    path('api/v1/', include(myapp_urls))
]


