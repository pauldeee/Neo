from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# @login_required # can use this decorator for areas where permission is required.
def account(request):
    if request.user.is_authenticated:
        return render(request, "account/account.html")
    else:
        return render(request, "authentication/signin.html")
