
from django import template
from django.forms.widgets import Select

register = template.Library()

@register.simple_tag
def administrator_active_list():
    return ['internationalregion', 'country', 'group', 'user', 'companysettings']

@register.simple_tag
def admin_active_list():
    return ['group', 'user', 'subscriptionplan', 'sitesettings', 'siteuser', 'logentry']

@register.filter
def is_select(field):
    return isinstance(field.field.widget, Select)

@register.filter
def is_allowed_admin(user_role):
    """Check if the user role is in the allowed roles."""
    allowed_roles = ['admin']
    return user_role in allowed_roles

@register.filter
def is_allowed_manager(user_role):
    """Check if the user role is in the allowed roles."""
    allowed_roles = ['manager', 'admin']
    return user_role in allowed_roles

@register.filter
def is_allowed_staff(user_role):
    """Check if the user role is in the allowed roles."""
    allowed_roles = ['staff', 'manager', 'admin']
    return user_role in allowed_roles
