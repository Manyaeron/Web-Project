
from rest_framework import permissions

from users.models import UserProfile
from .serializers import UserProfileSerializer

from rest_framework.generics import (
    ListAPIView
)

class UserProfileView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny, ) 