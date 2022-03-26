from django.contrib import admin
from django.urls import path, include

from pimo.views import PostAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pimo.urls')),
    path('api/v1/postlist/', PostAPIView.as_view())
]
