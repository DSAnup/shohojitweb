import os
from administrator.models import Country
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from imagekit.models import ProcessedImageField # type: ignore
from imagekit.processors import ResizeToFill # type: ignore

class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2, choices=Gender.choices, default=Gender.MALE, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_picture = ProcessedImageField(upload_to='users/profile_picture/',
                                           validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], 
                                           processors=[ResizeToFill(200, 200)],
                                           options={'quality': 70},  blank=True, null=True)
    personal_phone = models.CharField(max_length=20,  blank=True, null=True)
    work_phone = models.CharField(max_length=20,  blank=True, null=True)
    city = models.CharField(max_length=20,  blank=True, null=True)
    state = models.CharField(max_length=20,  blank=True, null=True)
    address = models.CharField(max_length=250,  blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_by_profile')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_by_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        if self.profile_picture:
            if os.path.isfile(self.profile_picture.path):
                os.remove(self.profile_picture.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username
