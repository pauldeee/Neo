from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# @login_required  # can use this decorator for areas where permission is required.
def account(request):
    if request.user.is_authenticated:
        print(request.user.exchange)
        print(request.user.api_key)
        print(request.user.api_secret)
        return render(request, "account/account.html")
    else:
        return render(request, "authentication/signin.html")


@login_required
def trading(request):
    return render(request, "account/trading.html")


@login_required
def news(request):
    return render(request, "account/news.html")


@login_required
def history(request):
    return render(request, "account/history.html")


@login_required
def api(request):
    return render(request, "account/api.html")


@login_required
def reports(request):
    return render(request, "account/reports.html")
