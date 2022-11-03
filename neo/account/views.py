import robin_stocks.robinhood.profiles
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TickerForm
from robin_stocks.robinhood.stocks import find_instrument_data as find_stocks
from robin_stocks.robinhood.crypto import get_crypto_currency_pairs as find_cryptos
from .robinhood import get_stocks_data
from .robinhood import get_my_account


# from robin_stocks.robinhood.crypto import


# Create your views here.
# @login_required  # can use this decorator for areas where permission is required.
def account(request):
    if request.user.is_authenticated:
        try:
            # context = {'my_account': robin_stocks.robinhood.profiles.load_account_profile()}
            robin_stocks.robinhood.authentication.login()
            context = {'my_account': get_my_account()}

            print(context)
            print('true')
            return render(request, "account/account.html", context)
        except:
            print('false')
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


# @TODO better error handling?!
@login_required
def search(request):
    if request.method == 'POST' and request.POST['ticker']:
        tid = request.POST['ticker']
        stocks = find_stocks(tid)
        try:
            tid = stocks[0]['symbol']
            return HttpResponseRedirect(tid)  # For now, just return the first result
        except:
            pass
    return render(request, 'account/account.html')


@login_required
def ticker(request, tid):
    robin_stocks.robinhood.authentication.login()
    context = {'ticker': tid,
               'stocks': get_stocks_data(tid),
               'price': robin_stocks.robinhood.stocks.get_latest_price(tid)
               }
    return render(request, 'account/ticker.html', context)
