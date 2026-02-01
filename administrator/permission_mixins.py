from django.contrib.auth.models import Permission
from django.db.utils import OperationalError, ProgrammingError

apps = ['userprofile']

def get_permission_add_list():
    try:
        permissions_add = Permission.objects.filter(
            content_type__app_label__in=apps,
            codename__startswith='add_'
        ).select_related('content_type')
        return tuple(
            f"{perm.content_type.app_label}.{perm.codename}" for perm in permissions_add
        )
    except (OperationalError, ProgrammingError):
        return ()

def get_permission_change_list():
    try:
        permissions_change = Permission.objects.filter(
            content_type__app_label__in=apps,
            codename__startswith='change_'
        ).select_related('content_type')
        return tuple(
            f"{perm.content_type.app_label}.{perm.codename}" for perm in permissions_change
        )
    except (OperationalError, ProgrammingError):
        return ()

def get_permission_delete_list():
    try:
        permissions_delete = Permission.objects.filter(
            content_type__app_label__in=apps,
            codename__startswith='delete_'
        ).select_related('content_type')
        return [
            f"{perm.content_type.app_label}.{perm.codename}" for perm in permissions_delete
        ]
    except (OperationalError, ProgrammingError):
        return []

# This is static, so it’s fine
AUTH_PERMISSION_LIST = (
    'auth.change_user',
    'auth.add_user',
    'auth.delete_user',
    'auth.view_user',
)
