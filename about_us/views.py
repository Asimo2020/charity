from django.shortcuts import render  
from accounts.models import User
from django.contrib.auth import get_user_model


def about_us(request):  
    users = User.objects.all()  
    return render(request, 'about_us.html', {'users': users})