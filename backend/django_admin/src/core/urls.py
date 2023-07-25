from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('notifications/', admin.site.urls),
    path('api/', include('api.urls')),
]
