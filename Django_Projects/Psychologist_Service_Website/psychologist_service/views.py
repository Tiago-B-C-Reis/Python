from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about_me.html')

def contacts(request):
    return render(request, 'contacts.html')

def services(request):
    return render(request, 'services.html')

def make_an_appointment(request):
    return render(request, 'make_an_appointment.html')

def resources(request):
    return render(request, 'resources.html')

# Add more view functions for additional pages as needed


# Run this in the terminal to launch the website:
# python manage.py runserver