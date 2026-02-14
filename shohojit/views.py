from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def teams(request):
    return render(request, 'teams.html')

def courses(request):
    return render(request, 'courses.html')

def course_detail(request, course_id):
    print(course_id)
    return render(request, 'course_detail.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')

def service_detail(request, service_id):
    print(service_id)
    return render(request, 'service_detail.html')

def contact(request):
    return render(request, 'contact.html')