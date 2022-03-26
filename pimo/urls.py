from django.urls import include, path
from rest_framework import routers
from pimo import views
from pimo.views import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
]

urlpatterns = [
    path('', views.orders_home, name='orders_home'),
]

urlpatterns = [
    path('', views.offers_home, name='offers_home'),
]

urlpatterns = [
    path('', views.users_home(), name='users_home'),
]

urlpatterns = [
    path('', views.offers_home, name='grades_home'),
]