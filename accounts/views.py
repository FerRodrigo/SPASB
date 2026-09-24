from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def login_view(request):
    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('home')