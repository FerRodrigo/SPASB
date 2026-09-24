from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date
import calendar
import json
from accounts.admin_login import custom_admin_login

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    from financeiro.models import Entrada, Despesa
    
    hoje = date.today()
    entradas = Entrada.objects.filter(data__month=hoje.month, data__year=hoje.year)
    despesas = Despesa.objects.filter(data__month=hoje.month, data__year=hoje.year)
    
    total_entradas = entradas.aggregate(Sum('valor_total'))['valor_total__sum'] or 0
    total_ong = entradas.aggregate(Sum('valor_ong'))['valor_ong__sum'] or 0
    total_vet = entradas.aggregate(Sum('valor_veterinaria'))['valor_veterinaria__sum'] or 0
    total_despesas = despesas.aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_ong - total_despesas
    
    contexto = {
        'total_entradas': total_entradas, 'total_ong': total_ong, 'total_vet': total_vet,
        'total_despesas': total_despesas, 'saldo': saldo,
        'ultimas_entradas': entradas.order_by('-data')[:5],
        'ultimas_despesas': despesas.order_by('-data')[:5],
    }
    return render(request, 'financeiro/dashboard.html', contexto)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', custom_admin_login, name='login'),
    path('financeiro/', include('financeiro.urls')),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
]
