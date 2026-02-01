from django.apps import AppConfig
from django.core.management import get_commands

class AdministratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'administrator'

    def ready(self):
        # Access and modify the command registry
        import administrator.signals
        commands = get_commands()
        if 'changepassword' in commands:
            del commands['changepassword']
        