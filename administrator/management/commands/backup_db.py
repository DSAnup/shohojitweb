import os
import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Backs up the database to a SQL file'

    def handle(self, *args, **options):
        
        DJANGO_ENV = os.getenv("DJANGO_ENV", "development")
        if DJANGO_ENV == "production":
            from adminsettings.production import DATABASES, DATABASE_ENGINE
        else:
            from adminsettings.development import DATABASES, DATABASE_ENGINE

        db_name = DATABASES['default']['NAME']
        backup_file = f'database/{db_name}_backup.sql'

        db_user = DATABASES['default']['USER']
        db_pass = DATABASES['default']['PASSWORD']
        db_host = DATABASES['default']['HOST']
        db_port = DATABASES['default']['PORT']

        if DATABASE_ENGINE == 'mysql':

            self.stdout.write(self.style.SUCCESS(f'MySQL debugging {db_user} {db_pass} {db_host} {db_port} {db_name} & Django {DJANGO_ENV}'))
            try:
                # Use subprocess and redirect output correctly
                with open(backup_file, 'w', encoding='utf-8') as f:
                    subprocess.run(
                        [
                            "mysqldump",
                            f"--user={db_user}",
                            f"--password={db_pass}",
                            f"--host={db_host}",
                            f"--port={str(db_port)}",
                            "--no-tablespaces",  # Optional
                            # "--skip-ssl",
                            db_name
                        ],
                        stdout=f,
                        stderr=subprocess.PIPE,
                        check=True
                    )
                if os.path.exists(backup_file):
                    self.stdout.write(self.style.SUCCESS(f'MySQL backup saved to {backup_file}'))
                else:
                    self.stdout.write(self.style.ERROR('MySQL backup file missing.'))
            except subprocess.CalledProcessError as e:
                self.stdout.write(self.style.ERROR(f'MySQL backup failed: {e.stderr.decode()}'))
        elif DATABASE_ENGINE == 'postgresql':
            env = os.environ.copy()
            env["PGPASSWORD"] = db_pass

            try:
                with open(backup_file, 'w', encoding='utf-8') as f:
                    subprocess.run(
                        [
                            "pg_dump",
                            "-h", db_host,
                            "-p", str(db_port),
                            "-U", db_user,
                            "-F", "p",  # plain SQL
                            db_name
                        ],
                        stdout=f,
                        stderr=subprocess.PIPE,
                        check=True,
                        env=env
                    )
                self.stdout.write(self.style.SUCCESS(f"PostgreSQL backup saved to {backup_file}"))
            except subprocess.CalledProcessError as e:
                self.stdout.write(self.style.ERROR(f"PostgreSQL backup failed: {e.stderr.decode()}"))
        else:
            backup_file = f'database/{os.path.basename(db_name)}_backup.sql'

            if os.path.exists(db_name):
                try:
                    subprocess.run(
                        ['sqlite3', db_name, '.dump'],
                        check=True,
                        stdout=open(backup_file, 'w', encoding='utf-8')
                    )
                    self.stdout.write(self.style.SUCCESS(f'SQLite backup saved to {backup_file}'))
                except subprocess.CalledProcessError as e:
                    self.stdout.write(self.style.ERROR(f'SQLite backup failed: {e}'))
