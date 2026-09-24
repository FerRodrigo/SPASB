from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.relatorio_mensal, name='inicio'),
    path('api/entradas/', views.api_entradas, name='api_entradas'),
    path('api/despesas/', views.api_despesas, name='api_despesas'),
    path('relatorio/', views.relatorio_mensal, name='relatorio_mensal'),
    path('relatorio/pdf/', views.relatorio_pdf, name='relatorio_pdf'),
    path('relatorio/excel/', views.relatorio_excel, name='relatorio_excel'),
    
    path('entrada/', views.entrada_list, name='entrada_list'),
    path('entrada/cadastrar/', views.entrada_create, name='entrada_create'),
    path('entrada/editar/<int:pk>/', views.entrada_edit, name='entrada_edit'),
    path('entrada/excluir/<int:pk>/', views.entrada_delete, name='entrada_delete'),
    
    path('despesa/', views.despesa_list, name='despesa_list'),
    path('despesa/cadastrar/', views.despesa_create, name='despesa_create'),
    path('despesa/editar/<int:pk>/', views.despesa_edit, name='despesa_edit'),
    path('despesa/excluir/<int:pk>/', views.despesa_delete, name='despesa_delete'),
]