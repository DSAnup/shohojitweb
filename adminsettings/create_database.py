import MySQLdb
from django.core.exceptions import ImproperlyConfigured
from adminsettings import development

def create_database_if_not_exists():
    db_name = development.DATABASES['default']['NAME']
    db_user = development.DATABASES['default']['USER']
    db_password = development.DATABASES['default']['PASSWORD']
    db_host = development.DATABASES['default']['HOST']
    db_port = development.DATABASES['default']['PORT']


    try:
        # Connect to MySQL
        conn = MySQLdb.connect(user=db_user, passwd=db_password, host=db_host, port=int(db_port))
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
        result = cursor.fetchone()

        if not result:
            # If the database does not exist, create it
            cursor.execute(f"CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            conn.commit()
            print(f"Database '{db_name}' created successfully.")

    except MySQLdb.Error as e:
        raise ImproperlyConfigured(f"Error creating database: {e}")
    
    finally:
        if conn:
            conn.close()

