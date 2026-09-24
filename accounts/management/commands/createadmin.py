from django.core.management.base import BaseCommand
from accounts.models import Usuario

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Usuario.objects.filter(username='admin').exists():
            Usuario.objects.create_superuser(
                username='admin',
                email='admin@spasb.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Usuário admin criado com sucesso!'))
        else:
            u = Usuario.objects.get(username='admin')
            u.set_password('admin')
            u.save()
            self.stdout.write(self.style.SUCCESS('Senha do admin atualizada!'))