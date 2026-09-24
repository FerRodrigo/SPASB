from rest_framework import serializers
from .models import Entrada, Despesa


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = [
            'id',
            'descricao',
            'tipo',
            'valor_total',
            'valor_ong',
            'valor_veterinaria',
            'data',
        ]
        
class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = [
            'id',
            'descricao',
            'tipo',
            'valor',
            'data',
        ]