from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    if request.method == 'POST':
        # Handling form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        User.objects.create(username=username, email=email)

    # Changing the text
    greeting = "Welcome to my website!"

    # Retrieving data from a table
    users = User.objects.all()

    context = {
        'greeting': greeting,
        'users': users,
    }

    return render(request, 'home.html', context)



def about(request):
    return render(request, 'about.html')

def another(request):
    return render(request, 'another.html')

def delete_info(request):
    # Delete the username and email here
    # Replace the code below with your logic
    username = ''
    email = ''
    
    return render(request, 'home.html', {'username': username, 'email': email})
