from django.test import TestCase
from .models import Entrada, Despesa
from .forms import EntradaForm, DespesaForm
from rest_framework.test import APIClient


class EntradaModelTest(TestCase):

    def test_divisao_valor_consulta(self):
        entrada = Entrada.objects.create(
            descricao='Teste de consulta',
            tipo='consulta',
            valor_total=100,
            data='2026-09-23'
        )

        self.assertEqual(entrada.valor_ong, 50)
        self.assertEqual(entrada.valor_veterinaria, 50)

    def test_valor_total_para_ong(self):
        entrada = Entrada.objects.create(
            descricao='Teste de adoção',
            tipo='adocao',
            valor_total=100,
            data='2026-09-23'
        )

        self.assertEqual(entrada.valor_ong, 100)
        self.assertEqual(entrada.valor_veterinaria, 0)


    def test_valor_zero_nao_e_permitido(self):
        form = EntradaForm(data={
            'descricao': 'Teste valor zero',
            'tipo': 'consulta',
            'valor_total': 0,
            'data': '2026-09-23'
        })

        self.assertFalse(form.is_valid())
        self.assertIn('valor_total', form.errors)




    def test_criacao_de_despesa(self):
        despesa = Despesa.objects.create(
            descricao='Teste de ração',
            tipo='racao',
            valor=100,
            data='2026-09-23'
        )

        self.assertEqual(despesa.descricao, 'Teste de ração')
        self.assertEqual(despesa.tipo, 'racao')
        self.assertEqual(despesa.valor, 100)




    def test_api_entradas(self):
        client = APIClient()

        Entrada.objects.create(
            descricao='Entrada API',
            tipo='consulta',
            valor_total=200,
            data='2026-09-23'
        )

        response = client.get('/financeiro/api/entradas/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['descricao'], 'Entrada API')
        self.assertEqual(response.data[0]['valor_total'], '200.00')




    def test_api_despesas(self):
        client = APIClient()

        Despesa.objects.create(
            descricao='Despesa API',
            tipo='racao',
            valor=150,
            data='2026-09-23'
        )

        response = client.get('/financeiro/api/despesas/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['descricao'], 'Despesa API')
        self.assertEqual(response.data[0]['valor'], '150.00')
