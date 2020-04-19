from django.core.management.base import BaseCommand, no_translations, CommandError
from login.models import User, Organisation as Org

class Command(BaseCommand):
    help = 'This should only be run once. This creates an admin "Organisation" and makes an admin superuser to help initially access the django admin site located at "/admin/", The flags should be used otherwise default values will be used'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help='Specifies the username')
        parser.add_argument('-fn', '--firstname', type=str, help='Specifies the first_name')
        parser.add_argument('-ln', '--lastname', type=str, help='Specifies the last_name')
        parser.add_argument('-p', '--password', type=str, help='Specifies the password')
        parser.add_argument('-e', '--email', type=str, help='Specifies the email to be used for both organisation and the admin user')
        parser.add_argument('-o', '--org', type=str, help='Specifies the organisation name which will be present only for admin')
        parser.add_argument('--default', action='store_true', help='sets default values')

    @no_translations
    def handle(self, *args, **options):

        defvals = [('username', 'admin'),
                ('firstname', 'admin'),
                ('lastname', ''),
                ('password', 'admin'),
                ('org', 'admin'),
                ('email', 'admin@admin.admin')]

        try:
            for i in defvals:
                if options[i[0]] == None:
                    if options['default']:
                        options[i[0]] = i[1]
                    else:
                        options[i[0]] = input(i[0] + ': ')

            r = Org.objects.filter(name=options['org'])
            if not r.count(): 
                admin_org = Org(name=options['org'], email=options['email'])
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
                        org=admin_org
                )
                self.stdout.write(self.style.SUCCESS('Superuser Created as: %s' % options['username']))
            else:
                self.stderr.write(self.style.ERROR('Superuser already exists as: %s' % options['username']))

        except KeyboardInterrupt:
            self.stderr.write(self.style.ERROR('User aborted the command'))
            

