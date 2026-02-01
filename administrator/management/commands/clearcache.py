# myapp/management/commands/clearcache.py

from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Clears the cache'

    def handle(self, *args, **options):
        # Clear cache
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Cache cleared successfully'))
