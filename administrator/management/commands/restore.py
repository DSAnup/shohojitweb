import sqlite3
import time
import os
import glob
import MySQLdb
from django.core.management.base import BaseCommand
from django.db import connections
from adminsettings.commonsettings import *
from adminsettings.settings import DJANGO_ENV

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
                
                # Load the database
                os.system(f'mysql -u {db_user} -p{db_password} {db_name} < database/{db_name}_backup.sql')
                self.stdout.write(self.style.SUCCESS(f'Database `{db_name}` loaded from database/{db_name}_backup.sql'))
            else:
                db_name = DATABASES['default']['NAME']
                # Ensure all DB connections are closed
                for conn in connections.all():
                    conn.close()

                # Give the system a short moment to release file handles
                time.sleep(0.5)

                if os.path.exists(db_name):
                    self.stdout.write(self.style.SUCCESS(f'SQLite3 debugging {db_name} & Django {DJANGO_ENV}'))
                    try:
                        os.remove(db_name)
                        self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` deleted.'))
                    except PermissionError as e:
                        self.stdout.write(self.style.ERROR(f'Could not delete SQLite DB: {e}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Database file `{db_name}` does not exist.'))
                # Load the database
                os.system(f'cp database/{db_name}_backup.sql  ')
                os.system('python manage.py makemigrations')
                os.system('python manage.py migrate')
                self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` loaded from database/{db_name}_backup.sql.'))
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
                
                # Load the database
                os.system(f'mysql -u {db_user} -p{db_password} {db_name} < database/{db_name}_backup.sql')
                self.stdout.write(self.style.SUCCESS(f'Database `{db_name}` loaded from database/{db_name}_backup.sql'))
            else:
                db_name = DATABASES['default']['NAME']
                backup_sql_file = f'database/{os.path.basename(db_name)}_backup.sql'
                # Ensure all DB connections are closed
                for conn in connections.all():
                    conn.close()

                # Give the system a short moment to release file handles
                time.sleep(0.5)

                # Delete old SQLite DB file if it exists
                if os.path.exists(db_name):
                    try:
                        os.remove(db_name)
                        self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` deleted.'))
                    except PermissionError as e:
                        self.stdout.write(self.style.ERROR(f'Could not delete SQLite DB due to permission error: {e}'))
                        # Abort here if you can't remove the old DB
                        return
                else:
                    self.stdout.write(self.style.WARNING(f'Database file `{db_name}` does not exist.'))

                # Check if backup SQL file exists
                if not os.path.exists(backup_sql_file):
                    self.stdout.write(self.style.ERROR(f'Backup SQL file `{backup_sql_file}` does not exist.'))
                    return

                # Restore the database from the SQL backup file
                try:
                    conn = sqlite3.connect(db_name)
                    cursor = conn.cursor()

                    with open(backup_sql_file, 'r', encoding='utf-8') as f:
                        sql_script = f.read()

                    cursor.executescript(sql_script)
                    conn.commit()
                    conn.close()

                    self.stdout.write(self.style.SUCCESS(f'SQLite3 database `{db_name}` restored from backup `{backup_sql_file}`.'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error while restoring SQLite DB: {e}'))
                    
        # Now create new migrations and apply them
        self.stdout.write(self.style.NOTICE('Creating new migrations...'))
        os.system('python manage.py makemigrations')

        self.stdout.write(self.style.NOTICE('Applying migrations to the database...'))
        os.system('python manage.py migrate')

        self.stdout.write(self.style.SUCCESS('Database restored and migrations reapplied successfully.'))



