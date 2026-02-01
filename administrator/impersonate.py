from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

@login_required
@user_passes_test(lambda u: u.is_superuser)
def impersonate_user(request, user_id):
    user_to_impersonate = get_object_or_404(User, pk=user_id)
    
    # Log out the current user (superuser)
    super_user_id = request.user.id
    logout(request)

    # Authenticate as the target user
    user_to_impersonate.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user_to_impersonate)
    request.session['original_user_id'] = super_user_id
    request.session['impersonating'] = True
    
    # Redirect to the desired page after impersonation
    return redirect('dashboard')  # replace 'home' with your target URL name

@login_required
def stop_impersonating(request):
    if not request.session.get('impersonating', False):
        return HttpResponseForbidden("You are not impersonating any user.")
    
    # Retrieve the original user id
    original_user_id = request.session.pop('original_user_id', None)
    original_user = get_object_or_404(User, pk=original_user_id)
    
    # Log out the impersonated user
    logout(request)
    
    # Authenticate as the original user
    original_user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, original_user)
    return redirect('dashboard')  # replace with your target URL name

