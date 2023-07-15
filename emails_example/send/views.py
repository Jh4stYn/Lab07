from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail('Hello from Django',
    'Hello there. This is an automated message.',
    'jhastyn57@gmail.com',
    ['jpayehuancar@unsa.edu.pe'],
    fail_silently=False)
    
    return render(request, 'send/index.html')