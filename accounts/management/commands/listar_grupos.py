from django.core.management.base import BaseCommand
from accounts.models import Usuario
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Cria usuário com grupo (Admin ou Financeiro)'

    def handle(self, *args, **options):
        # Verifica se admin existe
        admin_user = Usuario.objects.filter(username='admin').first()
        if admin_user:
            self.stdout.write(self.style.SUCCESS(f'Usuário admin: {admin_user.username}'))
            self.stdout.write(f'Grupos: {", ".join(admin_user.groups.all().values_list("name", flat=True) or ["Nenhum"])}')
        else:
            self.stdout.write(self.style.WARNING('Usuário admin não encontrado'))
        
        # Lista grupos
        grupos = Group.objects.all()
        if grupos:
            self.stdout.write(self.style.SUCCESS('\nGrupos disponíveis:'))
            for g in grupos:
                self.stdout.write(f'  - {g.name} ({g.permissions.count()} permissões)')
        else:
            self.stdout.write('Nenhum grupo encontrado')
