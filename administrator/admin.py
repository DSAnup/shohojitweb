
from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('iso2', 'country_name', 'calling_code', 'international_region')  # Customize the list display

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('international_region').order_by('iso2')
        return queryset
    search_fields = ('country_name',) 
admin.site.register(Country, CountryAdmin)