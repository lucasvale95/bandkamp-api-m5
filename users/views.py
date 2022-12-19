from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()