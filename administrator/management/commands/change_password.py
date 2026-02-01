from django.core.management import CommandError, BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a custom superuser.'
    
    def handle(self, *args, **kwargs):
        user = User.objects.get(username='anup')
        password = input('Enter password: ')
        user.set_password(password)
        user.save()
        self.stdout.write(self.style.SUCCESS("Superuser password change successfully."))
    