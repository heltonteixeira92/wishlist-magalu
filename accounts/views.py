from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .serializers import RegisterSerializer

UserModel = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
