from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from financeiro.models import Entrada, Despesa

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tipo', 'valor_total', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('descricao',)
    ordering = ('-data',)

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tipo', 'valor', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('descricao',)
    ordering = ('-data',)

admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Permission)