from django.contrib import admin
from django.urls import path, include
from myapp import urls as myapp_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(myapp_urls))
]
