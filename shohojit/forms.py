from django import forms
from administrator.mixins import  CustomWidgetMixin
from shohojit.models import ContactUs, Messages, Slider, HomeAboutFeature, GalleryCategory, GalleryImages,HomeAboutSection, Stats, TestimonialsImages, Testimonials 

class SliderForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'subtitle', 'image', 'is_active']

class HomeAboutSectionForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = HomeAboutSection
        fields = ['title', 'subtitle', 'description', 'image']

class HomeAboutFeatureForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = HomeAboutFeature
        fields = ['title', 'subtitle', 'icon_class']

class StatsForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['students', 'courses', 'projects', 'trainers']

class GalleryCategoryForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = GalleryCategory
        fields = ['name']

class GalleryImagesForm(CustomWidgetMixin, forms.ModelForm):
    category = forms.ModelChoiceField(queryset=GalleryCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Plan'}))
    class Meta:
        model = GalleryImages
        fields = ['category', 'title', 'subtitle', 'image']

class TestimonialsImagesForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = TestimonialsImages
        fields = ['images']

class TestimonialsForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['full_name', 'feedback']

class ContactUsForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['location', 'phone_number_one', 'phone_number_two', 'email_one', 'email_two', 'opening_hours']

class MessageForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['full_name', 'email', 'phone', 'service', 'subject', 'message']