import os
import glob
import MySQLdb
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connections
from adminsettings.commonsettings import *
from adminsettings.settings import DJANGO_ENV
from administrator.models import AccessModelName, SiteSettings, SiteUser

if DJANGO_ENV == "production":
    from adminsettings.production import *
else:
    from adminsettings.development import *


class Command(BaseCommand):
    help = 'Resets migrations and reapplies them.'

    def handle(self, *args, **kwargs):
        # Delete migration files
        for migration_file in glob.glob('*/migrations/*.py'):
            if not migration_file.endswith('__init__.py'):
                os.remove(migration_file)
        for migration_file in glob.glob('*/migrations/*.pyc'):
            os.remove(migration_file)

        # Optional: Drop and recreate the database if using SQLite
        if DJANGO_ENV == "production":
            if DATABASE_ENGINE == 'mysql':
                db_name = DATABASES['default']['NAME']
                db_user = DATABASES['default']['USER']
                db_password = DATABASES['default']['PASSWORD']
                db_host = DATABASES['default']['HOST']
                db_port = DATABASES['default']['PORT']

                # Connect to MySQL
                connection = MySQLdb.connect(user=db_user, passwd=db_password, host=db_host, port=int(db_port))

                cursor = connection.cursor()

                # Drop the database
                cursor.execute(f"DROP DATABASE IF EXISTS `{db_name}`;")
                self.stdout.write(self.style.SUCCESS(f'Database `{db_name}` dropped.'))

                # Create the database
                cursor.execute(f"CREATE DATABASE `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                self.stdout.write(self.style.SUCCESS(f'Database `{db_name}` created.'))

                # Close the connection
                cursor.close()
                connection.close()
            else:
                db_name = DATABASES['default']['NAME']
                if os.path.exists(db_name):
                    # Close SQLite connections
                    for conn in connections.all():
                        conn.close()
                    try:
                        os.remove(db_name)
                        self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` deleted.'))
                    except PermissionError as e:
                        self.stdout.write(self.style.ERROR(f'Could not delete SQLite DB: {e}'))
                self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` ready for migrations.'))
        else:
            if DATABASE_ENGINE == 'mysql':
                db_name = DATABASES['default']['NAME']
                db_user = DATABASES['default']['USER']
                db_password = DATABASES['default']['PASSWORD']
                db_host = DATABASES['default']['HOST']
                db_port = DATABASES['default']['PORT']

                # Connect to MySQL
                connection = MySQLdb.connect(user=db_user, passwd=db_password, host=db_host, port=int(db_port))

                cursor = connection.cursor()

                # Drop the database
                cursor.execute(f"DROP DATABASE IF EXISTS `{db_name}`;")
                self.stdout.write(self.style.SUCCESS(f'Database `{db_name}` dropped.'))

                # Create the database
                cursor.execute(f"CREATE DATABASE `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                self.stdout.write(self.style.SUCCESS(f'Database `{db_name}` created.'))

                # Close the connection
                cursor.close()
                connection.close()
            else:
                db_name = DATABASES['default']['NAME']
                if os.path.exists(db_name):
                    # Close SQLite connections
                    for conn in connections.all():
                        conn.close()
                    try:
                        os.remove(db_name)
                        self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` deleted.'))
                    except PermissionError as e:
                        self.stdout.write(self.style.ERROR(f'Could not delete SQLite DB: {e}'))
                self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` ready for migrations.'))
        # Run migrations
        os.system('python manage.py makemigrations')
        os.system('python manage.py migrate')

        os.system('python manage.py loaddata database/defaultuser.json')
        # Create superuser
        User = get_user_model()
        if not User.objects.filter(username='anup').exists():
            user = User.objects.create_superuser('anup', 'anup12.m@gmail.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Superuser created: anup / Admin@2024'))
        else:
            user = User.objects.get(username='anup')
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
            
        access_model_instance = AccessModelName.objects.get_or_create(identifier_name='default')
        if access_model_instance:
            self.stdout.write(self.style.WARNING('Defalut Access Model Created'))
        site_settings = SiteSettings.objects.get_or_create(pk=1)
        get_site_settings = SiteUser.objects.get_or_create(site= site_settings[0], user=user)
        
        os.system('python manage.py loaddata database/internationalregion.json')
        os.system('python manage.py loaddata database/country.json')
        os.system('python manage.py loaddata database/accessmodelname.json')
        os.system('python manage.py loaddata database/accessmodelname_content_type.json')
        os.system('python manage.py loaddata database/companysettings.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded databases'))
        os.system('python manage.py dumpdata --indent=2 --output=data.json')
        self.stdout.write(self.style.SUCCESS('Successfully store databases'))

        self.stdout.write(self.style.SUCCESS('Migrations have been reset, reapplied, and superuser created.'))
