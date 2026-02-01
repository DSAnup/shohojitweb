from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from userprofile.models import Profile

@login_required
def generate_pdf(request,  app_name,  model_name):
    model_class = apps.get_model(app_name, model_name)
    # Fetch the queryset
    queryset = model_class.objects.all()
    if model_name == 'user':
        exclude_fields = {'id', 'last_login', 'password', 'is_superuser', 'last_name'}
    else:
        exclude_fields = {'id', 'created_by', 'created_at', 'updated_by', 'updated_at'}
    headers = [field.name for field in model_class._meta.fields if field.name not in exclude_fields]  # Add column headers
    data = []
    for obj in queryset:
        row = []
        for column in headers:
            value = getattr(obj, column, None)
            row.append(value)
        data.append(row)  # Add rows

    context = {
        'title': f'{model_name} List',
        'headers': headers,
        'data': data,
        }
    html_string = render_to_string('generic/list.html', context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        filename = f"{model_name}_list.pdf"
        content = f"inline; filename={filename}"
        download = request.GET.get("download")
        if download:
            content = f"attachment; filename={filename}"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Error generating PDF")

@login_required
def generate_profile_pdf(request, pk):
    user_details = User.objects.get(id=pk)
    Profile.objects.get_or_create(user_id=pk)
    if user_details.profile.profile_picture:
        profile_picture_url = request.build_absolute_uri(user_details.profile.profile_picture.url)
    else:
        profile_picture_url = None

    context = {
        'user_details': user_details,
        'profile_picture_url': profile_picture_url,
    }
    html_string = render_to_string('generic/profile_pdf.html', context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        filename = f"Profile_{user_details.username}.pdf"
        content = f"inline; filename={filename}"
        download = request.GET.get("download")
        if download:
            content = f"attachment; filename={filename}"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Error generating PDF")