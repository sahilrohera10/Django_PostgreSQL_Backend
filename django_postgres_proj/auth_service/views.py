from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.

class UserRegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
