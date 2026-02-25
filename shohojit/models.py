import os
from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import User
from django.utils.text import slugify

class CommonFields(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_%(class)s')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_%(class)s')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)      
    image = ProcessedImageField(upload_to='sliders/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(1080, 600)], 
                                       options={'quality': 70},  blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_slider')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_slider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            old_instance = Slider.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except Slider.DoesNotExist:
            pass  # New object, no old image

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

class HomeAboutSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = ProcessedImageField(upload_to='about_section/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(600, 400)], 
                                       options={'quality': 70}, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_home_about_section')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_home_about_section')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            old_instance = HomeAboutSection.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except HomeAboutSection.DoesNotExist:
            pass  # New object, no old image

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
    
class HomeAboutFeature(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)  # Font Awesome icon class
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_home_about_feature')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_home_about_feature')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    practical_learning = models.CharField(max_length=50, blank=True, null=True)
    mentor_support = models.CharField(max_length=50, blank=True, null=True)
    real_projects = models.CharField(max_length=50, blank=True, null=True)
    course_image = ProcessedImageField(upload_to='courses/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(375, 180)], 
                                       options={'quality': 70}, blank=True, null=True)
    hero_image = ProcessedImageField(upload_to='course_hero_images/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(1080, 600)], 
                                       options={'quality': 70}, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_course')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.course_slug:
            self.course_slug = slugify(self.course_name)

        try:
            old_instance = Course.objects.get(pk=self.pk)
            if old_instance.course_image and old_instance.course_image != self.course_image:
                if os.path.isfile(old_instance.course_image.path):
                    os.remove(old_instance.course_image.path)
            if old_instance.hero_image and old_instance.hero_image != self.hero_image:
                if os.path.isfile(old_instance.hero_image.path):
                    os.remove(old_instance.hero_image.path)
        except Course.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.course_image and os.path.isfile(self.course_image.path):
            os.remove(self.course_image.path)
        if self.hero_image and os.path.isfile(self.hero_image.path):
            os.remove(self.hero_image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.course_name
    
class CourseHighlight(CommonFields):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='highlights')
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.course.course_name} - {self.title}"
    
class CourseCurriculum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='curriculums')
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=50, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)  # Font Awesome icon class
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_course_curriculum')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_course_curriculum')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.course_name} - {self.title}"

class CurriculumContent(CommonFields): 
    curriculum = models.ForeignKey(CourseCurriculum, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.curriculum.course.course_name} - {self.curriculum.title} - {self.title}"
    
class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    service_image = ProcessedImageField(upload_to='services/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(375, 180)], 
                                       options={'quality': 70}, blank=True, null=True)
    hero_image = ProcessedImageField(upload_to='service_hero_images/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(1080, 600)], 
                                       options={'quality': 70}, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)  # Font Awesome icon class
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_service')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_service')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.service_slug:
            self.service_slug = slugify(self.service_name)

        try:
            old_instance = Service.objects.get(pk=self.pk)
            if old_instance.service_image and old_instance.service_image != self.service_image:
                if os.path.isfile(old_instance.service_image.path):
                    os.remove(old_instance.service_image.path)
            if old_instance.hero_image and old_instance.hero_image != self.hero_image:
                if os.path.isfile(old_instance.hero_image.path):
                    os.remove(old_instance.hero_image.path)
        except Service.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.service_image and os.path.isfile(self.service_image.path):
            os.remove(self.service_image.path)
        if self.hero_image and os.path.isfile(self.hero_image.path):
            os.remove(self.hero_image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.service_name
    
class Stats(models.Model):
    students = models.IntegerField(default=0)
    courses = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    trainers = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_stats')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_stats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats: {self.students} students, {self.courses} courses, {self.projects} projects, {self.trainers} trainers"
    
class ContactUs(models.Model):
    location = models.CharField(max_length=200, blank=True, null=True)
    phone_number_one = models.CharField(max_length=20, blank=True, null=True)
    phone_number_two = models.CharField(max_length=20, blank=True, null=True)
    email_one = models.EmailField(blank=True, null=True)
    email_two = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_contactus')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_contactus')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number_one
    
class Messages(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True, related_name='messages') 
    message = models.TextField(blank=True, null=True)
    read_status = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_messages')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    
class Testimonials(models.Model):
    full_name = models.CharField(max_length=100)
    feedback = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_testimonials')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_testimonials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class TestimonialsImages(models.Model):
    images = ProcessedImageField(upload_to='testimonials/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(50, 50)], 
                                       options={'quality': 70}, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_testimonials_images')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_testimonials_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            old_instance = TestimonialsImages.objects.get(pk=self.pk)
            if old_instance.images and old_instance.images != self.images:
                if os.path.isfile(old_instance.images.path):
                    os.remove(old_instance.images.path)
        except TestimonialsImages.DoesNotExist:
            pass  # New object, no old image

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.images and os.path.isfile(self.images.path):
            os.remove(self.images.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.images.name
    
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_gallery_category')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_gallery_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class GalleryImages(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = ProcessedImageField(upload_to='gallery/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(800, 600)], 
                                       options={'quality': 70}, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_gallery_images')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_gallery_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            old_instance = GalleryImages.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except GalleryImages.DoesNotExist:
            pass  # New object, no old image

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
    
class TeamCategory(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_team_category')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_team_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TeamMembers(models.Model):
    category = models.ForeignKey(TeamCategory, on_delete=models.CASCADE, related_name='members')
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    profile_image = ProcessedImageField(upload_to='team_members/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(300, 300)], 
                                       options={'quality': 70}, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_team_members')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_team_members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            old_instance = TeamMembers.objects.get(pk=self.pk)
            if old_instance.profile_image and old_instance.profile_image != self.profile_image:
                if os.path.isfile(old_instance.profile_image.path):
                    os.remove(old_instance.profile_image.path)
        except TeamMembers.DoesNotExist:
            pass  # New object, no old image

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.profile_image and os.path.isfile(self.profile_image.path):
            os.remove(self.profile_image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.full_name
    

class AboutUs(models.Model):
    mission = models.TextField(max_length=500, blank=True, null=True)
    vision = models.TextField(max_length=500, blank=True, null=True)
    excelence = models.CharField(max_length=150, blank=True, null=True)
    innovation = models.CharField(max_length=150, blank=True, null=True)
    integrity = models.CharField(max_length=150, blank=True, null=True)
    empowerment = models.CharField(max_length=150, blank=True, null=True)
    image = ProcessedImageField(upload_to='about_us/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(1080, 600)], 
                                       options={'quality': 70}, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_about_us')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_about_us')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            old_instance = AboutUs.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except AboutUs.DoesNotExist:
            pass  # New object, no old image

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.excelence
    
class OurJourney(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_our_journey')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_our_journey')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_faq')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_faq')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


