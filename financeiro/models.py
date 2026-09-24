from django.db import models


class Entrada(models.Model):

    TIPO_ENTRADA = [
        ('consulta', 'Consulta'),
        ('castracao', 'Castração'),
        ('exame', 'Exame'),
        ('procedimento', 'Procedimento'),
        ('adocao', 'Taxa de adoção'),
        ('microchip', 'Microchip'),
        ('prefeitura', 'Verba da prefeitura'),
        ('outros', 'Outros'),
    ]

    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_ENTRADA)

    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    valor_ong = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False
    )

    valor_veterinaria = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False
    )

    data = models.DateField()

    def save(self, *args, **kwargs):

        if self.tipo in ['consulta', 'castracao', 'exame', 'procedimento']:

            self.valor_ong = self.valor_total / 2
            self.valor_veterinaria = self.valor_total / 2

        else:

            self.valor_ong = self.valor_total
            self.valor_veterinaria = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.descricao


class Despesa(models.Model):

    TIPO_DESPESA = [
        ('racao', 'Ração'),
        ('medicamentos', 'Medicamentos'),
        ('limpeza', 'Produtos de limpeza'),
        ('outros', 'Outros'),
    ]

    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_DESPESA)

    valor = models.DecimalField(max_digits=10, decimal_places=2)

    data = models.DateField()

    def __str__(self):
        return self.descricao