from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def faq(request):
    return render(request, "home/faq.html")


@login_required
def howto(request):
    return render(request, "home/howto.html")
