from django import forms
from django.contrib.auth.models import User, Group, Permission
from administrator.mixins import CleanValidation, CustomWidgetMixin
from administrator.models import Internationalregion, Country, CompanySettings, AccessModelName, SiteSettings, SiteUser, SubscriptionPlan, UserRole

class UserForm(CustomWidgetMixin, forms.ModelForm):
    try:
        access_model_instance = AccessModelName.objects.get(identifier_name='default')
        filtered_content_types = access_model_instance.content_type.values_list('model', flat=True)
    except:
        filtered_content_types = ['user', 'group']
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype your password', 'class': 'form-control required'}))
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id':'select-states1', 'placeholder': 'Available groups to add'})
        )
    role = forms.ChoiceField(
        choices=[choice for choice in UserRole.ROLE_CHOICES if choice[0] != 'admin'],
        initial='staff',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'groups']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) 
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['groups'].required = False
        if self.instance and self.instance.pk:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields.pop('password')
            self.fields.pop('password2')

            try:
                self.fields['role'].initial = self.instance.userrole.role
            except UserRole.DoesNotExist:
                self.fields['role'].initial = 'staff'

    def clean(self):
        cleaned_data = super().clean()
        
        if self.instance and self.instance.pk:
            return cleaned_data

        if self.request:
            if self.request.user.is_superuser:
                return cleaned_data

            site = getattr(self.request, 'site', None)
            if site and site.subscription_plan:
                limit = site.subscription_plan.user_limit
                current_count = SiteUser.objects.filter(site=site, is_active=True).count()
                
                if current_count >= limit:
                    raise forms.ValidationError(
                        f"Limit Reached: Your '{site.subscription_plan.plan_name}' plan "
                        f"only allows {limit} users. Please upgrade."
                    )
        return cleaned_data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']

        if data == '' or data is None:
            return data
        if not self.instance and not self.instance.pk:    
            if User.objects.filter(email=data).exists():
                raise forms.ValidationError('Email already in use.')
        return data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # If creating a new user or if password is provided, set the password
        if not self.instance.pk:  # New user
            user.set_password(self.cleaned_data['password'])
        elif 'password' in self.cleaned_data and self.cleaned_data['password']:  # If password is provided in edit form
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user.groups.set(self.cleaned_data['groups'])

            role, created = UserRole.objects.get_or_create(user=user)
            role.role = self.cleaned_data['role']
            role.save()

            SiteUser.objects.get_or_create(
                user=user, 
                site=self.request.site,
                defaults={'is_active': True, 'created_by': self.request.user}
            )
        
        return user
    
class UserFormSuper(CustomWidgetMixin, forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype your password', 'class': 'form-control required'}))
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id':'select-states1', 'placeholder': 'Available groups to add'})
        )
    
    is_staff = forms.BooleanField(label="Admin Status")
    role = forms.ChoiceField(
        choices=UserRole.ROLE_CHOICES, initial='staff',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active', 'groups']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) 
        super(UserFormSuper, self).__init__(*args, **kwargs)
        self.fields['groups'].required = False
        self.fields['is_staff'].required = False
        if self.instance and self.instance.pk:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields.pop('password')
            self.fields.pop('password2')

            try:
                self.fields['role'].initial = self.instance.userrole.role
            except UserRole.DoesNotExist:
                self.fields['role'].initial = 'staff'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']

        if data == '' or data is None:
            return data
        if not self.instance and not self.instance.pk:    
            if User.objects.filter(email=data).exists():
                raise forms.ValidationError('Email already in use.')
        return data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # If creating a new user or if password is provided, set the password
        if not self.instance.pk:  # New user
            user.set_password(self.cleaned_data['password'])
        elif 'password' in self.cleaned_data and self.cleaned_data['password']:  # If password is provided in edit form
            user.set_password(self.cleaned_data['password'])
        user.save()
        user.groups.set(self.cleaned_data['groups'])

        role, created = UserRole.objects.get_or_create(user=user)
        role.role = self.cleaned_data['role']
        role.save()

        return user
       
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype your password', 'class': 'form-control required'}))
    agree_to_terms = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email',]


    def clean_agree_to_terms(self):
        agree = self.cleaned_data.get('agree_to_terms')
        if not agree:
            raise forms.ValidationError("You must agree to the terms.")
        return agree
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']

        if data == '' or data is None:
            return data
            
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
class PasswordResetEmailForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control required'}))

    class Meta:
        model = User
        fields = ['email']
    
class UserPasswordUpdateForm(CustomWidgetMixin, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype your password',}))

    class Meta:
        model = User
        fields = ['password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control required'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'is_active'] 

class GroupForm(CustomWidgetMixin, forms.ModelForm):
    try:
        access_model_instance = AccessModelName.objects.get(identifier_name='default')
        filtered_content_types = access_model_instance.content_type.values_list('model', flat=True)
    except:
        filtered_content_types = ['user', 'group']
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.filter(content_type__model__in=filtered_content_types).select_related('content_type'), 
        widget=forms.CheckboxSelectMultiple,
        required=False  # optional, depending on your needs
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']

class GroupFormSuper(CustomWidgetMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.select_related('content_type').all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # optional, depending on your needs
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        

class InternationalregionForm(CustomWidgetMixin, forms.ModelForm):
    international_region_name = forms.CharField(widget=forms.TextInput(attrs={'class':'required'}))
    
    class Meta:
        model = Internationalregion
        fields = ['international_region_name']

    def clean(self):
        cleaned_data = super().clean()
        field_value = cleaned_data.get('international_region_name')
        CleanValidation.check_record_exists(self.__class__.__name__, 'international_region_name', field_value, self.instance)
        return cleaned_data

class CountryForm(CustomWidgetMixin, forms.ModelForm):
    international_region = forms.ModelChoiceField(
        queryset=Internationalregion.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select an Region'})
        )

    class Meta:
        model = Country
        fields = ['iso2', 'country_name', 'long_country_name', 'iso3', 'num_code', 'calling_code', 'international_region']

class CSVUploadForm(forms.Form):
    upload_file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.csv'}))

class CompanySettingsFormSuperUser(CustomWidgetMixin, forms.ModelForm):
    company_layout = forms.ChoiceField(choices=CompanySettings.LayoutChoice, widget=forms.Select(attrs={'class': 'form-control', 'id':'select-states1', 'placeholder': 'Choose your layout'}))
    
    class Meta:
        model = CompanySettings
        fields = ['company_name', 'company_email', 'company_phone', 'company_address', 'company_layout', 'company_logo', 'company_currency', 'company_menu_hover', 'company_import_option', 'company_export_pdf', 'company_export_csv', 'company_delete_all', 'company_datatable_column_visiable', 'company_datatable_csv', 'company_datatable_copy', 'company_datatable_excel', 'company_datatable_pdf', 'company_datatable_print', 'company_datatable_print_selected']  

class CompanySettingsForm(CustomWidgetMixin, forms.ModelForm):
    company_layout = forms.ChoiceField(choices=CompanySettings.LayoutChoice, widget=forms.Select(attrs={'class': 'form-control', 'id':'select-states1', 'placeholder': 'Choose your layout'}))
    
    class Meta:
        model = CompanySettings
        fields = ['company_name', 'company_email', 'company_phone', 'company_address', 'company_layout', 'company_menu_hover', 'company_logo']  

class AccessModelNameForm(CustomWidgetMixin, forms.ModelForm):

    class Meta:
        model = AccessModelName
        fields = ['identifier_name', 'content_type']
        widgets = {
            'content_type': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(AccessModelNameForm, self).__init__(*args, **kwargs)
        self.fields['identifier_name'].widget.attrs['readonly'] = True

class SubscriptionPlanForm(CustomWidgetMixin, forms.ModelForm):
    
    class Meta:
        model = SubscriptionPlan
        fields = ['plan_name', 'user_limit', 'plan_description']

class SiteSettingsForm(CustomWidgetMixin, forms.ModelForm):
    subscription_plan = forms.ModelChoiceField(queryset=SubscriptionPlan.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Plan'}))
    expired_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = SiteSettings
        fields = ['subscription_plan', 'is_subscription_active', 'expired_date', 'is_active', 'site_name', 'site_logo', 'site_title', 'site_owner', 'site_email', 'site_owner_phone', 'site_address']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if self.request and not self.request.user.is_superuser:
            self.fields['site_name'].disabled = True
            self.fields['subscription_plan'].disabled = True
            self.fields['is_subscription_active'].disabled = True
class SiteUserForm(CustomWidgetMixin, forms.ModelForm):
    site = forms.ModelChoiceField(queryset=SiteSettings.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Site'}))
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False, is_staff=True).order_by('username'), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states2', 'placeholder': 'Select a User'}))
    
    class Meta:
        model = SiteUser
        fields = ['site', 'user']
    
    def clean(self):
        cleaned_data = super().clean()  
        site = cleaned_data.get('site')
        user = cleaned_data.get('user')

        if SiteUser.objects.filter(site=site, user=user).exists():
            raise forms.ValidationError("This user is already assigned to this site.")
        
        return cleaned_data