from django import template

register = template.Library()

@register.filter
def has_select_field(form):
    """Check if the form has any select fields."""
    for field in form:
        if getattr(field.field.widget, 'input_type', '') == 'select':
            return True
    return False
