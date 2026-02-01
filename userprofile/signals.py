
import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from userprofile.models import Profile

@receiver(pre_save, sender=Profile)
def delete_old_profile_picture(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_picture = sender.objects.get(pk=instance.pk).profile_picture
    except sender.DoesNotExist:
        return False

    new_picture = instance.profile_picture
    if old_picture and old_picture != new_picture:
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)

@receiver(post_delete, sender=Profile)
def delete_profile_picture_on_delete(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)