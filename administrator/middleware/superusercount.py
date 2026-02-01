# myapp/middleware.py

from django.contrib.auth import get_user_model
from django.shortcuts import render

class SuperuserCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        User = get_user_model()
        superuser_count = User.objects.filter(is_superuser=True).count()
        usernames_to_exclude = ['anup', 'testuser']
        superusers_to_delete =User.objects.filter(is_superuser=True).exclude(username__in=usernames_to_exclude)
        # Delete the superusers
        superusers_to_delete.delete()
        
        if superuser_count > 1:
            return render(request, 'registration/superuserrestriction.html')

        response = self.get_response(request)
        return response
