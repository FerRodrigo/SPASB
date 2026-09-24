from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Usuario(AbstractUser):
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    cargo = models.CharField('Cargo', max_length=100, blank=True)
    data_cadastro = models.DateTimeField('Data de Cadastro', default=timezone.now)
    ultimo_acesso = models.DateTimeField('Último Acesso', null=True, blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.get_full_name() or self.username