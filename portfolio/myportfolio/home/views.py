from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def projects(request):
    return render(request, 'index/projects.html')

def certificates(request):
    return render(request, 'index/certificates.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f"Portfolio Message from {name}",
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        return redirect('contact')
    return render(request, 'index/contact.html')

