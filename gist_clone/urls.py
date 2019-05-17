from rest_framework import routers
from django.urls import path, include
from gist_clone.user.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # all the DRF routes at once.
    path('', include(router.urls)),
]
