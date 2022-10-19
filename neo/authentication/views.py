from django.contrib.auth import authenticate, login, logout
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
# def home(request):
#     return render(request, "home/home.html")


def signup(request):
    # I'm sure there's a better way to do this try-except block seems incorrectish
    try:
        if request.method == "POST":
            # username = request.POST.get('username')  # can also access like below
            user = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if not pass1:
                messages.error(request, "You must enter a password!")
                return render(request, 'authentication/signup.html')
            if not pass2:
                messages.error(request, "You must enter a second password!")
                return render(request, 'authentication/signup.html')
            if pass2 != pass1:
                messages.error(request, "Your passwords do not match!")
                return render(request, 'authentication/signup.html')
            my_user = User.objects.create_user(user, user, pass1)
            my_user.first_name = fname
            my_user.last_name = lname

            my_user.save()  # save the created user

            messages.success(request, "Your account has been successfully created.")
            return redirect('signin')
    except:
        messages.error(request, "This email is already in use. Please try another.")
        return render(request, 'authentication/signup.html')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        user = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=user, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "account/account.html")
        else:
            messages.error(request, "Log in failed! Please check the information you entered is accurate.")
            return render(request, 'authentication/signin.html')

    return render(request, "authentication/signin.html")
    # return render(request, "account/account.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
