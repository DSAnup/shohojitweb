import importlib
import os
from django import forms
from django.core.exceptions import ValidationError

class CustomWidgetMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Iterate through all fields and set attributes for their widgets
        for field_name, field in self.fields.items():
            if not isinstance(field, (forms.ChoiceField, forms.ModelChoiceField, forms.ModelMultipleChoiceField, forms.BooleanField, forms.DateField)):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': f'Enter {field_name.replace("_", " ").capitalize()}'
                    # Add more attributes if needed
                })

class CleanValidation:
    def check_record_exists(form_name, field_name, field_value, instance):
        # Your validation logic here, for example:
        if instance.pk is None:
            if instance.__class__.objects.filter(**{field_name: field_value}).exists():
                raise forms.ValidationError(f"The record '{field_value}' is already exists.")

def get_app_name(view_func):
    module = importlib.import_module(view_func.__module__)
    return module.__name__.split('.')[0]


# Validator function
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx']
    
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are: {", ".join(valid_extensions)}')
