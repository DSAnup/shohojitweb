from django import forms
from administrator.mixins import  CustomWidgetMixin
from shohojit.models import FAQ, AboutUs, ContactUs, CourseHighlight, CurriculumContent, Messages, OurJourney, Slider, HomeAboutFeature, GalleryCategory, GalleryImages,HomeAboutSection, Stats, TeamCategory, TeamMembers, TeamMembers, TestimonialsImages, Testimonials, Service, Course, CourseCurriculum

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

class AboutUsForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['excelence', 'integrity', 'innovation', 'empowerment', 'image', 'mission', 'vision']

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
        fields = ['location', 'phone_number_one', 'phone_number_two', 'email_one', 'email_two', 'opening_hours', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url']

class MessageForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['full_name', 'email', 'phone', 'service', 'subject', 'message']

class TeamCategoryForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = TeamCategory
        fields = ['name']

class TeamMembersForm(CustomWidgetMixin, forms.ModelForm):
    category = forms.ModelChoiceField(queryset=TeamCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Category'}))
    class Meta:
        model = TeamMembers
        fields = ['category', 'full_name', 'position', 'profile_image', 'linkedin_url', 'twitter_url', 'facebook_url', 'about_me']

class GalaryCategoryForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = GalleryCategory
        fields = ['name']

class GalleryImagesForm(CustomWidgetMixin, forms.ModelForm):
    category = forms.ModelChoiceField(queryset=GalleryCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Category'}))
    class Meta:
        model = GalleryImages
        fields = ['category', 'title', 'subtitle', 'image']

class ServicesForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'title', 'subtitle', 'service_image', 'icon_class', 'is_active', 'hero_image', 'service_description']

class CourseForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'title', 'subtitle', 'course_image', 'hero_image', 'duration', 'practical_learning', 'real_projects', 'is_active', 'course_description']

class CourseHighlightForm(CustomWidgetMixin, forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Course'}))  
    class Meta:
        model = CourseHighlight
        fields = ['course', 'title']

class CourseCurriculumForm(CustomWidgetMixin, forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Course'}))  
    class Meta:
        model = CourseCurriculum
        fields = ['course', 'title', 'duration', 'icon_class']

class CurriculumContentForm(CustomWidgetMixin, forms.ModelForm):
    curriculum = forms.ModelChoiceField(queryset=CourseCurriculum.objects.all(), widget=forms.Select(attrs={'class': 'form-control required', 'id':'select-states1', 'placeholder': 'Select a Curriculum'}))
    class Meta:
        model = CurriculumContent
        fields = ['curriculum', 'title']

class FaqForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

class OurJourneyForm(CustomWidgetMixin, forms.ModelForm):
    class Meta:
        model = OurJourney
        fields = ['title', 'year', 'short_description']