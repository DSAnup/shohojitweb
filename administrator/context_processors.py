from .models import CompanySettings, SiteUser
def company_settings(request):
    domainname = request.get_host()
    if request.user.is_authenticated:
        try:
            company_settings = CompanySettings.objects.get(owner=request.user)
        except CompanySettings.DoesNotExist:
            company_settings = None
    else:
        # If the user is anonymous, settings don't exist
        company_settings = None
    return {'company_settings': company_settings, 'domainname': domainname}
