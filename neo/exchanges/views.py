from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Exchange


# from .forms import ExchangeForm


# Create your views here.
def add_api(request):
    if request.method == 'POST':
        print(request.POST['api_key'])
        exchange = Exchange(
            exchange=request.POST['exchange'],
            api_key=request.POST['api_key'],
            api_secret=request.POST['api_secret']
        )
        exchange.save()
        messages.success(request, "Account has been successfully added!")
    return redirect('api')

# def get_exchanges(request):
#     exchanges = Exchange.EXCHANGES

# def new_form(request):
#     form = ExchangeForm(request.POST or None)
#     return render(request, 'authentication/api.html', {'form': form})
