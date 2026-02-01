from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from administrator.forms import UserUpdateForm
from userprofile.forms import ProfileUserForm
from userprofile.models import Profile
from .utils import resize_and_optimize_image


@login_required
def profile(request):
    return render(request, 'userprofile/profile.html')


@login_required
def profile_settings(request, id=None):
    if id:
        user = User.objects.get(pk=id)
    else:
        user = request.user
    try:
        user_profile = user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=user)
        user_profile.created_by = request.user
        user_profile.save()

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUserForm(request.POST, instance=user_profile, files=request.FILES)
        remove_picture = request.POST.get('profile_picture_clear')
        if user_form.is_valid() and profile_form.is_valid():
            
            user_form.save()
            user_profile = profile_form.save(commit=False)

            if user_profile.created_by:
                user_profile.updated_by = request.user

            if 'profile_picture' in request.FILES:
                user_profile.profile_picture = resize_and_optimize_image(request.FILES['profile_picture'], 200, 200)

            if remove_picture == 'on':
                user_profile.profile_picture.delete(save=False)
                
            user_profile.save()
            messages.success(request, 'Profile has been updated.')
            return redirect('profile_settings', user.pk)  # Redirect after success
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUserForm(instance=user_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'userprofile/settings.html', context)

