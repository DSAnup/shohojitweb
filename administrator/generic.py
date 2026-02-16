import os
import datetime
import json
import traceback
from django.apps import apps
from django.core.management import call_command
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import NoReverseMatch, reverse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode
from administrator.decorators import admin_only, staff_only, manager_only
from administrator.form_mapping import MODEL_FORM_MAPPING
from administrator.utils import log_admin_action
from adminsettings import settings

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


@login_required
@manager_only
def add(request, model_name, columns, m2m=None):
    model_name_lower = model_name.lower()
    if request.user.is_superuser and model_name_lower == 'user':
        form_class = MODEL_FORM_MAPPING.get('usersuper')
    elif request.user.is_superuser and model_name == 'group':
        form_class = MODEL_FORM_MAPPING.get('groupsuper')
    else:
        form_class = MODEL_FORM_MAPPING.get(model_name_lower)

    initial_data = {}
    if request.method == 'GET':
        for key, value in request.GET.items():
            initial_data[key] = value

    allowed_apps = ['']
    find_model = ContentType.objects.filter(model=model_name_lower, app_label__in=allowed_apps)
    add_request_model = ['user', 'sitesettings']
            
    if request.method == 'POST':
        if model_name_lower in add_request_model:   
            form = form_class(request.POST, request.FILES if request.FILES else None, request=request)
        else:
            form = form_class(request.POST, request.FILES if request.FILES else None)
        if form.is_valid():
            if model_name_lower == 'group':
                group = form.save()
                permissions = form.cleaned_data['permissions']
                group.permissions.set(permissions)
            else:
                created_record = form.save()
                created_record.created_by = request.user
                created_record.save()
                if find_model:
                    created_record.site = request.site.id
                if m2m is not None:
                    form.save_m2m()
                log_admin_action(request.user, created_record, ADDITION, f"Added {created_record}")
            messages.success(request, f'{model_name.capitalize()} Records created successfully.')
            
            view_name = f'list_{model_name_lower}'
            try:
                base_url = reverse(view_name)
            except NoReverseMatch:
                base_url = f'/{model_name_lower}/'
                
            params = {}
            if params:
                query_string = urlencode(params)
                return redirect(f"{base_url}?{query_string}")

            return redirect(base_url)
    else:
        if model_name_lower == 'user':   
            form = form_class(initial=initial_data, request=request)
        else:
            form = form_class(initial=initial_data)

    context = {
        'form': form, 
        'model_name': model_name,
        'page_label': 'add',
    }

    if columns == 1:
        return render(request, 'generic/generic_forms.html', context)
    elif columns == 2:
        return render(request, 'generic/generic_forms2.html', context)
    elif columns == 3:
        return render(request, 'generic/generic_forms2.html', context)
    else:
        return render(request, 'generic/generic_forms.html', context)

@login_required
@manager_only
def add_fk(request, model_name, app_name, field_name, fk_id, m2m=None):
    model_name_lower = model_name.lower()
    form_class = MODEL_FORM_MAPPING.get(model_name_lower)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES if request.FILES else None)
        if form.is_valid():
            created_record = form.save(commit=False)
            created_record.created_by = request.user
            related_model = apps.get_model(app_label=app_name, model_name=field_name.capitalize())
            fk_instance = related_model.objects.get(pk=fk_id)
            setattr(created_record, field_name, fk_instance)
            if hasattr(created_record, 'owner_user'):
                created_record.owner_user = request.user
            created_record.save()
            if m2m is not None:
                form.save_m2m()
            log_admin_action(request.user, created_record, ADDITION, f"Added Foreign Key {created_record}")
            messages.success(request, f'{model_name.capitalize()} Records created successfully.')
            return redirect(reverse(f'list_{model_name_lower}', kwargs={'fk_id': fk_id}))
    else:
        form = form_class()
            
    context = {
        'form': form, 
        'model_name': model_name,
        'fk_id': fk_id,
        'page_label': 'add_fk',
    }
    return render(request, 'generic/generic_forms_fk.html', context)
    
@login_required
@manager_only
def change(request, id, app_name, model_name, columns, m2m=None):
    model_class = apps.get_model(app_name, model_name)
    record = get_object_or_404(model_class, pk=id)
    model_name_lower = model_name.lower()
    if request.user.is_superuser and model_name_lower == 'user':
        form_class = MODEL_FORM_MAPPING.get('usersuper')
    elif request.user.is_superuser and model_name == 'group':
        form_class = MODEL_FORM_MAPPING.get('groupsuper')
    else:
        form_class = MODEL_FORM_MAPPING.get(model_name_lower)

    if request.method == 'POST':
        if model_name_lower == 'sitesettings':   
            form = form_class(request.POST, request.FILES if request.FILES else None, request=request, instance=record)
        else:
            form = form_class(request.POST, request.FILES if request.FILES else None, instance=record)
        if form.is_valid():
            if model_name_lower == 'group':
                group = form.save()
                permissions = form.cleaned_data['permissions']
                group.permissions.set(permissions)
            else:
                update_record = form.save(commit=False)
                update_record.updated_by = request.user
                update_record.save()
                if m2m is not None:
                    form.save_m2m()
                log_admin_action(request.user, update_record, CHANGE, f"Changed {update_record}")
            messages.success(request, f'{record} updated successfully.')
            
            view_name = f'list_{model_name_lower}'
            try:
                base_url = reverse(view_name)
            except NoReverseMatch:
                base_url = f'/{model_name_lower}/'
                
            params = {}
            if params:
                query_string = urlencode(params)
                return redirect(f"{base_url}?{query_string}")

            return redirect(base_url)
    else:
        if model_name_lower == 'sitesettings':   
            form = form_class(instance=record, request=request)
        else:
            form = form_class(instance=record)

    context = {
        'form': form, 
        'model_name': model_name,
        'page_label': 'change',
    }
    
    if columns == 1:
        return render(request, 'generic/generic_forms.html', context)
    elif columns == 2:
        return render(request, 'generic/generic_forms2.html', context)
    elif columns == 3:
        return render(request, 'generic/generic_forms2.html', context)
    else:
        return render(request, 'generic/generic_forms.html', context)

@login_required
@manager_only
def change_fk(request, id,  app_name,  model_name, fk_id):
    model_class = apps.get_model(app_name, model_name)
    record = get_object_or_404(model_class, pk=id)
    model_name_lower = model_name.lower()
    form_class = MODEL_FORM_MAPPING.get(model_name_lower)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES if request.FILES else None, instance=record)
        if form.is_valid():
            update_record = form.save(commit=False)
            update_record.updated_by = request.user
            update_record.save()
            log_admin_action(request.user, update_record, CHANGE, f"Changed Foreign Key {update_record}")
            messages.success(request, f'{record} updated successfully.')
            return redirect(reverse(f'list_{model_name_lower}', kwargs={'fk_id': fk_id}))
    else:
        form = form_class(instance=record)

    context = {
        'form': form, 
        'model_name': model_name,
        'fk_id': fk_id,
        'page_label': 'change',
    }
    return render(request, 'generic/generic_forms_fk.html', context)

@login_required
@staff_only
def view(request, id,  app_name,  model_name, columns, m2m=None):
    model_class = apps.get_model(app_name, model_name)
    record = get_object_or_404(model_class, pk=id)
    model_name_lower = model_name.lower()
    if request.user.is_superuser and model_name_lower == 'user':
        form_class = MODEL_FORM_MAPPING.get('usersuper')
    else:
        form_class = MODEL_FORM_MAPPING.get(model_name_lower)
        
    if model_name_lower == 'expense':
        form = form_class(instance=record, user=request.user)
    else:
        form = form_class(instance=record)

    context = {
        'form': form, 
        'model_name': model_name,
        'page_label': 'view',
    }

    return render(request, 'generic/generic_forms_view.html', context)


@login_required
@staff_only
def view_fk(request, id,  app_name,  model_name, fk_id):
    model_class = apps.get_model(app_name, model_name)
    record = get_object_or_404(model_class, pk=id)
    model_name_lower = model_name.lower()
    if request.user.is_superuser and model_name_lower == 'user':
        form_class = MODEL_FORM_MAPPING.get('usersuper')
    else:
        form_class = MODEL_FORM_MAPPING.get(model_name_lower)
        
    if model_name_lower == 'expense':
        form = form_class(instance=record, user=request.user)
    else:
        form = form_class(instance=record)

    context = {
        'form': form, 
        'model_name': model_name,
        'fk_id': fk_id,
        'page_label': 'view',
    }

    return render(request, 'generic/generic_forms_view_fk.html', context)

@login_required
@admin_only
def delete(request, id, app_name,  model_name):
    model_class = apps.get_model(app_name, model_name)
    record = get_object_or_404(model_class, pk=id)
    record.delete()
    log_admin_action(request.user, record, DELETION, f"Deleted {record}")
    messages.success(request, f"Record '{record}' has been successfully deleted.")
    return redirect(f'list_{model_name}')


@login_required
@admin_only
def delete_fk(request, id, app_name,  model_name, fk_id):
    model_class = apps.get_model(app_name, model_name)
    record = get_object_or_404(model_class, pk=id)
    record.delete()
    log_admin_action(request.user, record, DELETION, f"Deleted Foreign Key {record}")
    messages.success(request, f"Record '{record}' has been successfully deleted.")
    return redirect(reverse(f'list_{model_name}', kwargs={'fk_id': fk_id}))


@csrf_exempt
def delete_multiple(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('selected_ids')
        model = data.get('model_name')
        app_lebel = data.get('app_name')
        model_class = apps.get_model(app_lebel, model)
        model_class.objects.filter(id__in=ids).delete()
        messages.success(request, "Record's has been successfully deleted.")
        response_data = {
            'message': 'success'
        }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)



def backup_database(request):
    try:
        call_command('backup_db')
    except Exception as e:
        error_message = traceback.format_exc()
        # Log to file for debugging
        with open('database/backup_error.log', 'w') as f:
            f.write(error_message)
        return HttpResponse("Backup failed. Check server logs.", status=500)

    # Get DB config
    db_settings = settings.DATABASES['default']
    db_engine = db_settings['ENGINE']
    db_name = db_settings['NAME']

    # Determine expected backup file path
    if 'sqlite3' in db_engine:
        backup_filename = f"{os.path.basename(db_name)}_backup.sql"
    else:
        backup_filename = f"{db_name}_backup.sql"

    backup_path = os.path.join('database', backup_filename)

    # Ensure the backup file exists
    if os.path.exists(backup_path):
        with open(backup_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/sql')
            response['Content-Disposition'] = f'attachment; filename="{backup_filename}"'
            return response
    else:
        return HttpResponse('Backup file not found.', status=404)