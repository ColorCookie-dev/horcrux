from django.core import management
from django.core.management.base import BaseCommand, no_translations, CommandError

class Command(BaseCommand):
    help = "Quick and dirty setup for the project"

    def handle(self, *args, **options):
        management.call_command('migrate', '--run-syncdb')
        self.stdout.write(self.style.SUCCESS('Migrated the models'))
        management.call_command('create_admin', default=True)
        self.stdout.write(self.style.SUCCESS('Created admin with username: admin, password: admin'))
