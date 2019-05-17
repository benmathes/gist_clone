from rest_framework import viewsets

from gist_clone.user.models import User
from gist_clone.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
