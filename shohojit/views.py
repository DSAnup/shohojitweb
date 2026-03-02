from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.shortcuts import render, redirect
from shohojit.models import FAQ, AboutUs, ContactUs, Course, GalleryCategory, GalleryImages, HomeAboutFeature, HomeAboutSection, Messages, OurJourney, Slider, Stats, TeamCategory, TeamMembers, Testimonials, TestimonialsImages

@ratelimit(key='ip', rate='5/m', block=True)
def index(request):

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Messages.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
    
        return JsonResponse({
            "status": "success",
            "message": "Your message has been sent successfully!"
        })

    
    sliders = Slider.objects.filter(is_active=True)[:5]
    stats = Stats.objects.first()
    homeabout = HomeAboutSection.objects.first()
    aboutfeature = HomeAboutFeature.objects.all().order_by('-created_at')[:3]
    contact_us = ContactUs.objects.first()
    testiominals = Testimonials.objects.all().order_by('-created_at')[:3]
    testimonial_images = TestimonialsImages.objects.all().order_by('-created_at')[:6]
    courses = Course.objects.filter(is_active=True).order_by('-created_at')[:6]
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    galleries = GalleryImages.objects.order_by('?')[:6]

    context = {
        'sliders': sliders,
        'stats': stats,
        'homeabout': homeabout,
        'aboutfeature': aboutfeature,
        'contact_us': contact_us,
        'testiominals': testiominals,
        'testimonial_images': testimonial_images,
        'courses': courses,
        'galleries': galleries,
        'course_list': course_list
    }
    return render(request, 'index.html', context)

def about(request):
    about_us = AboutUs.objects.first()
    homeabout = HomeAboutSection.objects.first()
    teams = TeamMembers.objects.all().order_by('id')[:8]
    our_journey = OurJourney.objects.all()
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    contact_us = ContactUs.objects.first()

    context = {
        'about_us': about_us,
        'teams': teams,
        'our_journey': our_journey,
        'contact_us': contact_us,
        'course_list': course_list,
        'homeabout': homeabout
    }
    return render(request, 'about.html', context)

def teams(request):
    team_category = TeamCategory.objects.all()
    teams = TeamMembers.objects.all().select_related('category')
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    contact_us = ContactUs.objects.first()

    context = {
        'team_category': team_category,
        'teams': teams,
        'contact_us': contact_us,
        'course_list': course_list
    }
    return render(request, 'teams.html', context)

def courses(request):
    courses = Course.objects.filter(is_active=True).order_by('-created_at')
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    contact_us = ContactUs.objects.first()

    context = {
        'courses': courses,
        'contact_us': contact_us,
        'course_list': course_list
    }
    return render(request, 'courses.html', context)

def course_detail(request, course_slug):
    course_detail = Course.objects.get(course_slug=course_slug)
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    contact_us = ContactUs.objects.first()

    context = {
        'course_detail': course_detail,
        'contact_us': contact_us,
        'course_list': course_list
    }
    return render(request, 'course_detail.html', context)

def gallery(request):
    gallery_category = GalleryCategory.objects.all()
    galleries = GalleryImages.objects.all().select_related('category')
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    contact_us = ContactUs.objects.first()
    
    context = {
        'gallery_category': gallery_category,
        'galleries': galleries,
        'contact_us': contact_us,
        'course_list': course_list
    }
    return render(request, 'gallery.html', context)

def services(request):
    return render(request, 'services.html')

def service_detail(request, service_id):
    print(service_id)
    return render(request, 'service_detail.html')

@ratelimit(key='ip', rate='5/m', block=True)
def contact(request):
    course_list = Course.objects.filter(is_active=True)[:6].values('course_name', 'course_slug')
    contact_us = ContactUs.objects.first()
    faqs = FAQ.objects.all().order_by('-created_at')

    if request.method == 'POST':
        # Get data from the form
        if request.method == "POST":
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Messages.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
        
            return JsonResponse({
                "status": "success",
                "message": "Your message has been sent successfully!"
            })
    context = {
        'contact_us': contact_us,
        'faqs': faqs,
        'course_list': course_list
    }
    return render(request, 'contact.html', context)