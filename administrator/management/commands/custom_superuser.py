from django.core.management import CommandError, BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a custom superuser.'
    
    def handle(self, *args, **kwargs):
        User = get_user_model()

        if User.objects.filter(is_superuser=True).count() > 2:
            raise CommandError("PLEASE CONTACT YOUR SOFTWARE SUPPORT STAFF.")
        
        username = input('Enter username: ')
        email = input('Enter email: ')
        password = input('Enter password: ')

        if not username or not email or not password:
            raise CommandError("All fields (username, email, password) are required...")

        if User.objects.filter(username=username).exists():
            raise CommandError("Username already exists.")
        
        if User.objects.filter(email=email).exists():
            raise CommandError("Email already exists.")

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))
    