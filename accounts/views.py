from django.shortcuts import render 
from accounts.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LogoutAPIView(APIView):
    pass


class UserRegistration(generics.CreateAPIView):
    pass
def about_us(request): 
    users = User.objects.all() 
    return render(request, 'about_us.html', {'users': users})