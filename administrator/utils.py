from django.contrib.admin.models import LogEntry
from django.contrib.admin.models import ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType

def log_admin_action(user, obj, action_flag, message=""):
    """
    Logs admin actions safely using Django 6+ API (log_actions).
    """
    if not user or not obj:
        return
    try:
        LogEntry.objects.log_action(
        user_id=user.pk,
        content_type_id=ContentType.objects.get_for_model(obj).pk,
        object_id=obj.pk,
        object_repr=str(obj),
        action_flag=action_flag,
        change_message=message,
    )

    except Exception as e:
        print("Admin logging failed:", e)
