from django import forms
from administrator.mixins import CustomWidgetMixin
from administrator.models import Country
from .models import Profile

class ProfileUserForm(CustomWidgetMixin, forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states', 'placeholder': 'Select an Country'}), 
        required=False
    )
    sex = forms.ChoiceField(choices=Profile.Gender, widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states2', 'placeholder': 'Select an Sex'}), required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/jpeg, image/png'}), required=False)

    class Meta:
        model = Profile
        fields = ['sex', 'dob', 'profile_picture', 'personal_phone', 'work_phone', 'address', 'city', 'state', 'country']    