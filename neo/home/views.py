from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def faq(request):
    return render(request, "home/faq.html")


def howto(request):
    return render(request, "home/howto.html")
