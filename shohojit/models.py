from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)      
    image = ProcessedImageField(upload_to='sliders/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(1080, 600)], 
                                       options={'quality': 70},  blank=True, null=True)
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
    def __str__(self):
        return self.title
    
class HomeAboutFeature(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)  # Font Awesome icon class
    def __str__(self):
        return self.title
    
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_highlight = models.TextField(blank=True, null=True)
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
    def __str__(self):
        return self.course_name
    
class CourseCurriculum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='curriculums')
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=50, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)  # Font Awesome icon class
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.course.course_name} - {self.title}"
    
class service(models.Model):
    service_name = models.CharField(max_length=200)
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
    def __str__(self):
        return self.service_name
    
class stats(models.Model):
    students = models.IntegerField(default=0)
    courses = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    trainers = models.IntegerField(default=0)
    def __str__(self):
        return f"Stats: {self.students} students, {self.courses} courses, {self.projects} projects, {self.trainers} trainers"
    
class contactus(models.Model):
    location = models.CharField(max_length=200, blank=True, null=True)
    phone_number_one = models.CharField(max_length=20, blank=True, null=True)
    phone_number_two = models.CharField(max_length=20, blank=True, null=True)
    email_one = models.EmailField(blank=True, null=True)
    email_two = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.phone_number
    
class messages(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    
    
class testimonials(models.Model):
    full_name = models.CharField(max_length=100)
    feedback = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.full_name
    
class testimonials_images(models.Model):
    images = ProcessedImageField(upload_to='testimonials/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(50, 50)], 
                                       options={'quality': 70}, blank=True, null=True)
    def __str__(self):
        return self.images.name
    
class gallery_category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class gallery_images(models.Model):
    category = models.ForeignKey(gallery_category, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = ProcessedImageField(upload_to='gallery/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(800, 600)], 
                                       options={'quality': 70}, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class team_category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class team_members(models.Model):
    category = models.ForeignKey(team_category, on_delete=models.CASCADE, related_name='members')
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
    def __str__(self):
        return self.full_name
    

class about_us(models.Model):
    mission = models.TextField(max_length=500, blank=True, null=True)
    vission = models.TextField(max_length=500, blank=True, null=True)
    excelence = models.CharField(max_length=150, blank=True, null=True)
    innovation = models.CharField(max_length=150, blank=True, null=True)
    integrity = models.CharField(max_length=150, blank=True, null=True)
    empowerment = models.CharField(max_length=150, blank=True, null=True)
    image = ProcessedImageField(upload_to='about_us/', 
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])], 
                                       processors=[ResizeToFill(1080, 600)], 
                                       options={'quality': 70}, blank=True, null=True)
    def __str__(self):
        return self.excelence
    
class our_mission(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class faq(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.question
    
