from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, DestroyAPIView

from .models import MyUser
from .serializers import UserSerializer


class UserList(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserDetails(RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserCreate(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserDelete(DestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
