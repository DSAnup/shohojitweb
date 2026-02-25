import os
from smtplib import SMTPException
from django.contrib import messages
from django.contrib.admin.models import LogEntry
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.cache import never_cache
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from administrator.decorators import manager_only, staff_or_permission_required
from administrator.forms import CompanySettingsFormSuperUser, PasswordResetEmailForm, UserPasswordUpdateForm, UserRegistrationForm, CompanySettingsForm, AccessModelNameForm
from administrator.mixins import get_app_name
from administrator.models import Internationalregion, Country, CompanySettings, AccessModelName, SiteSettings, SiteUser, SubscriptionPlan
from administrator.utils import log_admin_action
from django.contrib.admin.models import ADDITION, CHANGE, DELETION
from adminsettings import commonsettings
from adminsettings.settings import DJANGO_ENV
from shohojit.models import FAQ, AboutUs, ContactUs, Course, CourseCurriculum, CourseHighlight, CurriculumContent, GalleryCategory, GalleryImages, HomeAboutFeature, HomeAboutSection, Messages, OurJourney, Service, Slider, Stats, TeamCategory, TeamMembers, Testimonials, TestimonialsImages
from shohojit.forms import AboutUsForm, ContactUsForm, ContactUsForm, HomeAboutSectionForm, HomeAboutSectionForm, StatsForm

@never_cache
def user_login(request):
    config = commonsettings.DASHBOARD_CONFIG
    if config == 'web':
        login_template = 'registration/login.html'
    else:
        login_template = 'registration/login_soft.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Authentication successful.')
                
                if remember_me == 'on':
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    request.session.set_expiry(0)
                
                log_admin_action(request.user, user, ADDITION, f'Login Successful {user.username}')
                return redirect('dashboard')
            else:
                messages.error(request, 'Disabled account.')
                return render(request, login_template)
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, login_template)

    else:
        return render(request, login_template)
    
def user_logout(request):
    user = request.user
    logout(request)
    log_admin_action(user, user, DELETION, f'Logout Successful {user.username}')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/signup_complete.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': user_form})

def password_reset_request(request):

    domain_name = request.get_host()
    if request.is_secure():
        protocol_use = 'https'
    else:
        protocol_use = 'http'

    try:
        company = CompanySettings.objects.get(pk=1)
        company_name = company.company_name
        company_email = company.company_email
    except CompanySettings.DoesNotExist:
        company_name = 'WAPS SOULUTIONS'
        company_email = 'no-reply@wapssolution.com'
        
    if company_email == None:
        company_email = 'no-reply@wapssolution.com'

    if request.method == 'POST':
        password_form = PasswordResetEmailForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data.get('email')
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Reset Request'
                    email_template_name = 'registration/password_reset_email.html'
                    parameters = {
                        'email': user.email,
                        'domain': domain_name,
                        'site_name': company_name,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': protocol_use
                    }
                    email_body = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email_body, company_email, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    except SMTPException as e:
                        return HttpResponse(f"SMTP error occurred: {e}")
                    except ValidationError as e:
                        return HttpResponse(f"Validation error: {e}")
                    except Exception as e:
                        return HttpResponse(f'Invalid exception: {e}')
                    log_admin_action(request.user, user, CHANGE, f'Password Reset Request {request.user}')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetEmailForm()
    context = {
        'password_form': password_form, 
    }
    return render(request, 'registration/password_reset.html', context)

@login_required
def password_change_request(request):
    if request.method == 'POST':
        form = UserPasswordUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            log_admin_action(request.user, user, CHANGE, f'Password Changed {request.user}')
            messages.success(request, 'Your password has been changed.')
        else:
            messages.error(request, 'Please correct the errors.')
    else:
        form = UserPasswordUpdateForm()
    context = {
        'form': form, 
    }
    return render(request, 'administrator/password_change_form.html', context)

@login_required
@staff_or_permission_required('auth.view_user')
def list_user(request):
    if request.user.is_superuser:
        users = User.objects.exclude(id=request.user.id)
    else:
        users = User.objects.exclude(id=request.user.id).filter(is_superuser=False)
    context = {
        'users': users, 
        'model_name': 'user',
        'app_name' : 'auth',
        'columns' : 2
    }
    return render(request, 'administrator/admin/user/list_user.html', context)

@login_required
@staff_or_permission_required('auth.view_group')
def list_group(request):
    group = Group.objects.all()
    context = {
        'groups': group, 
        'model_name': 'group',
        'app_name' : 'auth',
        'columns' : 2
    }
    return render(request, 'administrator/admin/group/list_group.html', context)

@login_required
@staff_or_permission_required('admin.view_logentry')
def list_logentry(request):
    log_entries = LogEntry.objects.all().order_by('-action_time')
    context = {
        'log_entries': log_entries, 
        'model_name': 'logentry',
        'app_name' : 'admin',
        'columns' : 2
    }
    return render(request, 'administrator/admin/logentry/list_logentry.html', context)

@login_required
@staff_or_permission_required('administrator.view_country')
def list_country(request):
    country_list = Country.objects.all().select_related('international_region')
    app_name = get_app_name(list_country)
    context = {
        'country_list': country_list, 
        'model_name': 'country',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'administrator/country/list_country.html', context)

@login_required
@staff_or_permission_required('administrator.view_internationalregion')
def list_internationalregion(request):
    international_region_list = Internationalregion.objects.all()
    app_name = get_app_name(list_internationalregion)
    context = {
        'international_region_list': international_region_list, 
        'model_name': 'internationalregion',
        'app_name' : app_name,
        'columns' : 1
    }
    return render(request, 'administrator/international_region/list_international_region.html', context)

@login_required
@staff_or_permission_required('administrator.view_companysettings')
def company_settings(request):
    company_default_settings, created = CompanySettings.objects.get_or_create(owner=request.user)
    remove_picture = request.POST.get('company_logo-clear')
    if request.method == 'POST':
        if request.user.is_superuser:
            form = CompanySettingsFormSuperUser(request.POST, instance=company_default_settings, files=request.FILES)
        else:
            form = CompanySettingsForm(request.POST, instance=company_default_settings, files=request.FILES)
        if company_default_settings.company_logo:
            image_path = company_default_settings.company_logo.path
        if form.is_valid():
            company_form = form.save(commit=False)
            if company_default_settings.created_by:
                company_form.updated_by = request.user
            else:
                company_form.created_by = request.user

            if remove_picture == 'on':
                if os.path.exists(image_path):
                    os.remove(image_path)
            company_form.save()
            messages.success(request, 'Company settings has been updated.')
            log_admin_action(request, company_form, CHANGE, f'Company settings updated {company_form}')
            return redirect('company_settings') 
    else:
        if request.user.is_superuser:
            form = CompanySettingsFormSuperUser(instance=company_default_settings)
        else:
            form = CompanySettingsForm(instance=company_default_settings)

    app_name = get_app_name(company_settings)
    context = {
        'model_name': 'companysettings',
        'app_name' : app_name,
        'form': form,
    }

    return render(request, 'administrator/company_settings.html', context)

@login_required
@staff_or_permission_required('administrator.view_accessmodelname')
def access_model_add(request):
    access_model_record, created = AccessModelName.objects.get_or_create(identifier_name='default')
    
    if request.method == 'POST':
        form = AccessModelNameForm(request.POST, instance=access_model_record)
        if form.is_valid():
            access_model_form = form.save(commit=False)
            if access_model_record.created_by:
                access_model_form.updated_by = request.user
            else:
                access_model_form.created_by = request.user
            access_model_form.save()
            form.save_m2m()
            messages.success(request, 'Access model settings has been updated.')
            return redirect('access_model_settings') 
    else:
        form = AccessModelNameForm(instance=access_model_record)

    app_name = get_app_name(access_model_add)
    context = {
        'model_name': 'accessmodelname',
        'app_name' : app_name,
        'form': form,
    }

    return render(request, 'administrator/access_model_settings.html', context)

@login_required
@require_POST
def toggle_user_active_status(request):
    user_id = request.POST.get("user_id")
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    log_admin_action(request.user, user, CHANGE, f"User active status changed {user}")
    return JsonResponse({"is_active": user.is_active})

@login_required
@require_POST
def toggle_user_admin_status(request):
    user_id = request.POST.get("user_id")
    user = get_object_or_404(User, id=user_id)
    user.is_staff = not user.is_staff
    user.save()
    log_admin_action(request.user, user, CHANGE, f"User admin status changed {user}")
    return JsonResponse({"is_staff": user.is_staff})
@login_required
@staff_or_permission_required('administrator.view_subscriptionplan')
def list_subscriptionplan(request):
    subscription_plan_list = SubscriptionPlan.objects.all()
    app_name = get_app_name(list_subscriptionplan)
    context = {
        'subscription_plan_list': subscription_plan_list, 
        'model_name': 'subscriptionplan',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'administrator/admin/list_subscription_plan.html', context)

@login_required
@staff_or_permission_required('administrator.view_sitesettings')
def list_sitesettings(request):
    if request.user.is_superuser:
        list_sitesettings = SiteSettings.objects.all()
    else:
        list_sitesettings = SiteSettings.objects.filter(site_settings__user=request.user)

    app_name = get_app_name(list_sitesettings)
    context = {
        'sitesetting_list': list_sitesettings, 
        'model_name': 'sitesettings',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'administrator/admin/list_sitesettings.html', context)

@login_required
@staff_or_permission_required('administrator.view_siteuser')
def list_siteuser(request):
    siteuser_list = SiteUser.objects.all().select_related('site', 'user')
    app_name = get_app_name(list_siteuser)
    context = {
        'siteuser_list': siteuser_list, 
        'model_name': 'siteuser',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'administrator/admin/list_siteuser.html', context)
@login_required
@manager_only
def list_slider(request):
    slider_list = Slider.objects.all()
    app_name = 'shohojit'
    context = {
        'slider_list': slider_list, 
        'model_name': 'slider',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_slider.html', context)

@login_required
@manager_only
def list_homeaboutfeature(request):
    home_about_feature_list = HomeAboutFeature.objects.all()
    app_name = 'shohojit'
    context = {
        'home_about_feature_list': home_about_feature_list, 
        'model_name': 'homeaboutfeature',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_home_about_feature.html', context)

@login_required
@manager_only
def list_testimonials(request):
    testimonials_list = Testimonials.objects.all()
    app_name = 'shohojit'
    context = {
        'testimonials_list': testimonials_list, 
        'model_name': 'testimonials',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_testimonials.html', context)

@login_required
@manager_only
def list_testimonialsimages(request):
    testimonials_images_list = TestimonialsImages.objects.all()
    app_name = 'shohojit'
    context = {
        'testimonials_images_list': testimonials_images_list, 
        'model_name': 'testimonialsimages',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_testimonials_images.html', context)

@login_required
@manager_only
def list_teamcategory(request):
    team_category_list = TeamCategory.objects.all()
    app_name = 'shohojit'
    context = {
        'team_category_list': team_category_list, 
        'model_name': 'teamcategory',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_team_category.html', context)

@login_required
@manager_only
def list_teammembers(request):
    team_members_list = TeamMembers.objects.all().select_related('category')
    app_name = 'shohojit'
    context = {
        'team_members_list': team_members_list, 
        'model_name': 'teammembers',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_team_members.html', context)

@login_required
@manager_only
def list_gallerycategory(request):
    gallery_category_list = GalleryCategory.objects.all()
    app_name = 'shohojit'
    context = {
        'gallery_category_list': gallery_category_list, 
        'model_name': 'gallerycategory',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_gallery_category.html', context)

@login_required
@manager_only
def list_galleryimages(request):
    gallery_images_list = GalleryImages.objects.all().select_related('category')
    app_name = 'shohojit'
    context = {
        'gallery_images_list': gallery_images_list, 
        'model_name': 'galleryimages',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_gallery_images.html', context)

@login_required
@manager_only
def list_messages(request):
    messages_list = Messages.objects.all().select_related('service')
    app_name = 'shohojit'
    context = {
        'messages_list': messages_list, 
        'model_name': 'messages',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_messages.html', context)

@login_required
@manager_only
def list_service(request):
    service_list = Service.objects.all()
    app_name = 'shohojit'
    context = {
        'service_list': service_list, 
        'model_name': 'service',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_services.html', context)

@login_required
@manager_only
def list_faq(request):
    faq_list = FAQ.objects.all()
    app_name = 'shohojit'
    context = {
        'faq_list': faq_list, 
        'model_name': 'faq',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_faq.html', context)

@login_required
@manager_only
def list_ourjourney(request):
    our_journey_list = OurJourney.objects.all()
    app_name = 'shohojit'
    context = {
        'our_journey_list': our_journey_list, 
        'model_name': 'ourjourney',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_our_journey.html', context)

@login_required
@manager_only
def list_course(request):
    course_list = Course.objects.all()
    app_name = 'shohojit'
    context = {
        'course_list': course_list, 
        'model_name': 'course',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_course.html', context)

@login_required
@manager_only
def list_coursehighlight(request):
    coursehighlight_list = CourseHighlight.objects.all().select_related('course')
    app_name = 'shohojit'
    context = {
        'coursehighlight_list': coursehighlight_list, 
        'model_name': 'coursehighlight',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_coursehighlight.html', context)

@login_required
@manager_only
def list_coursecurriculumn(request):
    coursecurriculumn_list = CourseCurriculum.objects.all().select_related('course')
    app_name = 'shohojit'
    context = {
        'coursecurriculumn_list': coursecurriculumn_list, 
        'model_name': 'coursecurriculumn',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_coursecurriculumn.html', context)

@login_required
@manager_only
def list_curriculumncontent(request):
    curriculumncontent_list = CurriculumContent.objects.all().select_related('curriculum')
    app_name = 'shohojit'
    context = {
        'curriculumncontent_list': curriculumncontent_list, 
        'model_name': 'curriculumncontent',
        'app_name' : app_name,
        'columns' : 2
    }
    return render(request, 'list_curriculumncontent.html', context)

@login_required
@manager_only
def stats_settings(request):
    stats, created = Stats.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = StatsForm(request.POST, instance=stats)
        if form.is_valid():
            stats_form = form.save(commit=False)
            if stats.created_by:
                stats_form.updated_by = request.user
            else:
                stats_form.created_by = request.user
            stats_form.save()
            messages.success(request, 'Stats settings has been updated.')
            log_admin_action(request, stats_form, CHANGE, f'Stats settings updated {stats_form}')
            return redirect('stats_settings') 
    else:
        form = StatsForm(instance=stats)

    app_name = get_app_name(stats_settings)
    context = {
        'model_name': 'stats',
        'app_name' : app_name,
        'form': form,
    }

    return render(request, 'stats_settings.html', context)

@login_required
@manager_only
def home_about_section_settings(request):
    home_about_section, created = HomeAboutSection.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = HomeAboutSectionForm(request.POST, instance=home_about_section, files=request.FILES)
        if form.is_valid():
            home_about_section_form = form.save(commit=False)
            if home_about_section.created_by:
                home_about_section_form.updated_by = request.user
            else:
                home_about_section_form.created_by = request.user
            home_about_section_form.save()
            messages.success(request, 'Home about section settings has been updated.')
            log_admin_action(request, home_about_section_form, CHANGE, f'Home about section settings updated {home_about_section_form}')
            return redirect('home_about_section_settings') 
    else:
        form = HomeAboutSectionForm(instance=home_about_section)

    app_name = get_app_name(home_about_section_settings)
    context = {
        'model_name': 'homeaboutsection',
        'app_name' : app_name,
        'form': form,
    }

    return render(request, 'home_about_section_settings.html', context)


@login_required
@manager_only
def about_us_settings(request):
    about_us, created = AboutUs.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, instance=about_us, files=request.FILES)
        if form.is_valid():
            about_us_form = form.save(commit=False)
            if about_us.created_by:
                about_us_form.updated_by = request.user
            else:
                about_us_form.created_by = request.user
            about_us_form.save()
            messages.success(request, 'About us settings has been updated.')
            log_admin_action(request, about_us_form, CHANGE, f'About us settings updated {about_us_form}')
            return redirect('about_us_settings') 
    else:
        form = AboutUsForm(instance=about_us)

    app_name = get_app_name(about_us_settings)
    context = {
        'model_name': 'aboutus',
        'app_name' : app_name,
        'form': form,
    }

    return render(request, 'about_us_settings.html', context)
@login_required
@manager_only
def contact_us_settings(request):
    contact_us, created = ContactUs.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contact_us)
        if form.is_valid():
            contact_us_form = form.save(commit=False)
            if contact_us.created_by:
                contact_us_form.updated_by = request.user
            else:
                contact_us_form.created_by = request.user
            contact_us_form.save()
            messages.success(request, 'Contact us settings has been updated.')
            log_admin_action(request, contact_us_form, CHANGE, f'Contact us settings updated {contact_us_form}')
            return redirect('contact_us_settings') 
    else:
        form = ContactUsForm(instance=contact_us)

    app_name = get_app_name(contact_us_settings)
    context = {
        'model_name': 'contactus',
        'app_name' : app_name,
        'form': form,
    }

    return render(request, 'contact_us_settings.html', context)

@login_required
def dashboard(request):
    return render(request, 'administrator/dashboard.html')