import os
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField # type: ignore
from imagekit.processors import ResizeToFill # type: ignore
from django.contrib.contenttypes.models import ContentType

class Internationalregion(models.Model):
    international_region_name = models.CharField(max_length=80)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_region')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_region')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.international_region_name

class Country(models.Model):
    iso2 = models.CharField(max_length=2)
    country_name = models.CharField(max_length=80)
    long_country_name = models.CharField(max_length=80, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    num_code = models.CharField(max_length=6, blank=True, null=True)
    calling_code = models.CharField(max_length=8, blank=True, null=True)
    international_region = models.ForeignKey(Internationalregion, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_country')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_country')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name
   
class CompanySettings(models.Model):
    class LayoutChoice(models.TextChoices):
        DEFAULT = 'D', 'Dafault'
        ASIDE = 'A', 'Aside'
        STICKY = 'S', 'Sticky'
        STICKY_OVERLAP = 'SO', 'Sticky Overlap'
        OVERLAP = 'O', 'Overlap'

    company_name = models.CharField(max_length=200, default='Waps Solution')
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    company_email = models.EmailField(max_length=150, blank=True, null=True)
    company_logo = ProcessedImageField(upload_to='company/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(300, 88)], 
                                       options={'quality': 70},  blank=True, null=True)
    company_address = models.CharField(max_length=250, blank=True, null=True)
    company_layout = models.CharField(max_length=2, choices=LayoutChoice.choices, default=LayoutChoice.DEFAULT, blank=True, null=True)
    company_menu_hover= models.BooleanField(default=False)
    company_import_option = models.BooleanField(default=False)
    company_export_pdf = models.BooleanField(default=False)
    company_export_csv = models.BooleanField(default=False)
    company_delete_all = models.BooleanField(default=False)
    company_datatable_column_visiable= models.BooleanField(default=False)
    company_datatable_csv= models.BooleanField(default=False)
    company_datatable_copy= models.BooleanField(default=False)
    company_datatable_excel= models.BooleanField(default=False)
    company_datatable_pdf= models.BooleanField(default=False)
    company_datatable_print= models.BooleanField(default=False)
    company_datatable_print_selected= models.BooleanField(default=False)
    company_currency= models.CharField(max_length=3, blank=True, null=True, default='$')
    company_currency_name= models.CharField(max_length=3, blank=True, null=True, default='USD')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_companysettings')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_companysettings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        if self.company_logo:
            if os.path.isfile(self.company_logo.path):
                os.remove(self.company_logo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.company_name

class AccessModelName(models.Model):
    identifier_name = models.CharField(default="default", max_length=15)
    content_type = models.ManyToManyField(ContentType)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_access')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_access')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.identifier_name
    
class SubscriptionPlan(models.Model):
    plan_name = models.CharField(max_length=100, default='Free')
    user_limit = models.IntegerField(default=2)
    plan_description = models.TextField(default="This is a free plan")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_subscriptionplan')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_subscriptionplan')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default='wapssolution')
    site_title = models.CharField(max_length=200, default='wapssolution')
    site_owner = models.CharField(max_length=200, blank=True, null=True)
    site_email = models.EmailField(max_length=150, blank=True, null=True)
    site_owner_phone = models.CharField(max_length=20, blank=True, null=True)
    site_address = models.CharField(max_length=250, blank=True, null=True)
    site_logo = ProcessedImageField(upload_to='site_logo/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(300, 88)], 
                                       options={'quality': 70},  blank=True, null=True)
    is_subscription_active = models.BooleanField(default=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, blank=True, null=True)
    expired_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_sitesettings')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_sitesettings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='site_user')
    site = models.ForeignKey(SiteSettings, on_delete=models.SET_NULL, blank=True, null=True, related_name='site_settings')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_siteuser')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_siteuser')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
class UserRole(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} - {self.role}"