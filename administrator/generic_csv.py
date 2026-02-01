import csv
import datetime
import os
from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render, redirect, HttpResponse
from administrator.forms import CSVUploadForm

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@login_required
def create_csv(request, app_name, model_name):
    model_class = apps.get_model(app_name, model_name)
    directory_path = os.path.join(settings.MEDIA_ROOT, f'csv/{model_name}')

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    csv_file_path = os.path.join(directory_path, f'{model_name}.csv')
    
    exclude_fields = {'id', 'created_by', 'created_at', 'updated_by', 'updated_at'}
    field_names = []
    for field in model_class._meta.get_fields():
        if isinstance(field, models.Field) and field.blank is False and not field.auto_created and field.name not in exclude_fields:
            field_names.append(field.name)

    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field_names)
        messages.success(request, 'csv file created successfully.')
    return redirect(f'/import/csv/{app_name}/{model_name}')

@login_required
def export_to_csv(request, app_name,  model_name):
    response = HttpResponse(content_type='text/csv')
    filename = f"{model_name}_{timestamp}.csv"
    response['Content-Disposition'] = f'attachment; filename= "{filename}"'
    model_class = apps.get_model(app_name, model_name)

    writer = csv.writer(response)
    queryset = model_class.objects.all()

    exclude_fields = {'id', 'created_by', 'created_at', 'updated_by', 'updated_at'}
    field_names = [field.name for field in model_class._meta.fields if field.name not in exclude_fields]
    writer.writerow(field_names)

    for obj in queryset:
        row = [getattr(obj, field) for field in field_names]
        writer.writerow(row)

    return response

@login_required
def upload_csv_file(request, app_name, model_name):
    model_class = apps.get_model(app_name, model_name)
    file_path = os.path.join(settings.MEDIA_ROOT, f'csv/{model_name}/{model_name}.csv')
    file_exists = os.path.exists(file_path)
    if file_exists:
        file_url = os.path.join(settings.MEDIA_URL, f'csv/{model_name}/{model_name}.csv')
    else:
        file_url = None

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['upload_file']

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            data_count = 0
            for row in reader:
                first_key, first_value = next(iter(row.items()))
                keys_list = list(row.keys())
                for field in model_class._meta.get_fields():
                    if field.name in keys_list:
                        if isinstance(field, ForeignKey):
                            related_model = field.related_model
                            try:
                                related_value = related_model.objects.get(id=row[field.name])
                                if field.name in row:
                                    row[field.name] = related_value 
                            except related_model.DoesNotExist as e:
                                messages.error(request, e)
                                return redirect(f'/import/csv/{app_name}/{model_name}')
                            except ValueError as e:
                                messages.error(request, e)
                                return redirect(f'/import/csv/{app_name}/{model_name}')
                        if row[field.name] == '':
                            messages.error(request, f'{field.name} should not be empty. please assign appropriate value.')
                            return redirect(f'/import/csv/{app_name}/{model_name}')
                    
                if not model_class.objects.filter(**{first_key:first_value}).exists():
                    try:
                        new_object = model_class(**row)
                        new_object.created_by=request.user.pk
                        new_object.save()
                        data_count += 1
                    except ValueError as e:
                        messages.error(request, f'{e}')
                        return redirect(f'/import/csv/{app_name}/{model_name}')
                    
            if data_count > 0:
                messages.success(request, f'{data_count} records successfully uploaded')
            else:
                messages.error(request, 'records are already exists')
            return redirect(f'list_{model_name}')
    else:
        form = CSVUploadForm()
    context = {
        'model_name': model_name,
        'page_label': 'upload',
        'form': form,
        'app_name': app_name,
        'file_exists': file_exists,
        'file_url': file_url,
    }
    return render(request, 'generic/import_csv.html', context)
