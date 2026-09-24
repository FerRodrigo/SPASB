from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def custom_admin_login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            context['error'] = True
    
    return render(request, 'admin/login.html', context)