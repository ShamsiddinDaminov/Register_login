from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'apps/home.html')


def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Confrom_password = request.POST['Confrom_password']
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        return HttpResponse("Registered successfully")
        # print(uname, email, password, Confrom_password)

    return render(request, 'apps/register.html')


def login(request):
    return render(request, 'apps/login.html')
