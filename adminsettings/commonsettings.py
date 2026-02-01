from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DASHBOARD_CONFIG = 'software' 


SECRET_KEY = 'django-insecure-9g^ecq3m5%rfhe6&f$w76%*5g4$w=0xwmvowq(8@mq5&(+z*&j'

INSTALLED_APPS = [
    #Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 
    # Add project apps
    'administrator',
    'userprofile',
    # library apps
    'imagekit',
]   

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'administrator.middleware.superusercount.SuperuserCountMiddleware',
    'administrator.middleware.APICallMiddleware.APICallMiddleware',
    "administrator.middleware.SiteMiddleware.SiteMiddleware",
]


# Add Custom authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'administrator.authentication.EmailAuthBackend',
]

DATABASE_NAME = 'admin_db'
DATABASE_ENGINE = 'mysql'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}