from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    

    return render(request, 'index.html')
