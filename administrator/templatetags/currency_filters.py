from django import template

register = template.Library()

@register.filter
def format_currency(value, currency):
    """Format a value with the currency symbol inside the negative sign."""
    try:
        value = float(value)  # Ensure the value is numeric
        if value < 0:
            return f"-{currency}{abs(value):,.2f}"  # Negative case
        return f"{currency}{value:,.2f}"  # Positive case
    except (ValueError, TypeError):
        return f"{currency}0.00"  # Default for invalid values
