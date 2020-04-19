from django.core.management.base import BaseCommand, no_translations, CommandError
from login.models import User, Organisation as Org

class Command(BaseCommand):
    help = 'This should only be run once. This creates an admin "Organisation" and makes an admin superuser to help initially access the django admin site located at "/admin/", The flags should be used otherwise default values will be used'

    def add_arguments(self, parser):
        self.defvals = [
                ('username', str, 'admin'),
                ('firstname', str, 'admin'),
                ('lastname', str, ''),
                ('password', str, 'admin'),
                ('org', str, 'admin'),
                ('email', str, 'admin@admin.admin'),
                ('VAT', int, 123),
                ('CIN', int, 123),
                ('postcode', int, 123),
                ('addr', str, '123, This Street'),
                ('website', str, 'example.com'),
                ('phone', int, 123),]

        for i in self.defvals:
            parser.add_argument('--' + i[0], type=i[1], help='Specifies the ' + i[0])

        parser.add_argument('--default', action='store_true', help='sets default values')

    @no_translations
    def handle(self, *args, **options):
        try:
            for i in self.defvals:
                if options[i[0]] == None:
                    if options['default']:
                        options[i[0]] = i[2]
                    else:
                        options[i[0]] = i[1](input(i[0] + ': '))

            r = Org.objects.filter(name=options['org'])
            if not r.count(): 
                admin_org = Org(
                        name=options['org'],
                        email=options['email'],
                        VAT=options['VAT'],
                        CIN=options['CIN'],
                        phone=options['phone'],
                        website=options['website'],
                        postcode=options['postcode'],
                        addr=options['addr'],
                    )
                admin_org.save()
                self.stdout.write(self.style.SUCCESS('Admin Organisation Created as: %s' % options['org']))
            else:
                admin_org = Org.objects.get(name=options['org'])
                self.stderr.write(self.style.ERROR('Admin Organisation already exists as: %s' % options['org']))

            r = User.objects.filter(username=options['username'])
            if not r.count():
                User.objects.create_superuser(
                        first_name=options['firstname'],
                        last_name=options['lastname'],
                        username=options['username'],
                        email=admin_org.email,
                        password=options['password'],
                        org=admin_org,
                        phone=options['phone'],
                        postcode=options['postcode'],
                        addr=options['addr'],
                    )
                self.stdout.write(self.style.SUCCESS('Superuser Created as: %s' % options['username']))
            else:
                self.stderr.write(self.style.ERROR('Superuser already exists as: %s' % options['username']))

        except KeyboardInterrupt:
            self.stderr.write(self.style.ERROR('User aborted the command'))
            

