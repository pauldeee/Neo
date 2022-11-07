import django.utils.datetime_safe
import robin_stocks.robinhood.profiles
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from plotly.subplots import make_subplots
from robin_stocks.robinhood.stocks import find_instrument_data as find_stocks
from plotly.offline import plot
import plotly.graph_objects as go
import cufflinks as cf

import pandas as pd

from .forms import OrderForm
from .robinhood import get_my_account
from .robinhood import get_stocks_data


# from robin_stocks.robinhood.crypto import


# Create your views here.
# @login_required  # can use this decorator for areas where permission is required.
def account(request):
    if request.user.is_authenticated:
        try:
            # context = {'my_account': robin_stocks.robinhood.profiles.load_account_profile()}
            robin_stocks.robinhood.authentication.login()
            context = {'account': robin_stocks.robinhood.profiles.load_account_profile(),
                       'portfolio': robin_stocks.robinhood.load_portfolio_profile(),
                       'holdings': robin_stocks.robinhood.account.build_holdings(),
                       'cryptos': robin_stocks.robinhood.crypto.get_crypto_positions(),
                       'orders': robin_stocks.robinhood.account.get_open_stock_positions(),
                       # 'stock_pairs': robin_stocks.robinhood.markets.get_all_stocks_from_market_tag(tag='technology')
                       }
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
    return redirect('account')


@login_required
def ticker(request, tid):
    robin_stocks.robinhood.authentication.login()  # login the user, not sure why this needs to be called in different views? maybe different instances of logins?
    hist = robin_stocks.robinhood.stocks.get_stock_historicals(tid, interval='day', span='year')
    hist_df = pd.DataFrame.from_dict(hist)

    candlesticks = go.Candlestick(
        x=hist_df['begins_at'],
        open=hist_df['open_price'],
        high=hist_df['high_price'],
        low=hist_df['low_price'],
        close=hist_df['close_price'],
        increasing_line_color='cyan',
        decreasing_line_color='pink', showlegend=False)
    volume_bars = go.Bar(
        x=hist_df['begins_at'],
        y=hist_df['volume'],
        showlegend=False,
        marker={"color": "rebeccapurple"}
    )

    start = hist_df.iloc[0, 0]
    end = hist_df.iloc[len(hist_df) - 1, 0]
    print(start)
    print(end)

    dt_all = pd.date_range(start=start, end=end)

    dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(hist_df['begins_at'])]

    dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if d not in dt_obs]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(candlesticks, secondary_y=True)
    fig.add_trace(volume_bars, secondary_y=False)
    fig.update_xaxes(
        rangebreaks=[
            dict(values=dt_breaks),
        ])
    fig.update_yaxes(gridcolor='black', secondary_y=False, showgrid=False)
    fig.update_yaxes(title_text='Price $', secondary_y=True, showgrid=True, gridcolor='black')
    fig.update_layout(
        # xaxis_title='Date',
        yaxis_title="Volume $",
        # width=600,
        height=600,
        plot_bgcolor='gray',
    )

    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'Date',
        'yaxis_title': 'Price',
        'height': 200,
        'width': 200,
    }

    plot_div = plot({'data': fig, 'layout': layout}, output_type='div')

    order_form = OrderForm()

    context = {'ticker': tid,
               'stocks': get_stocks_data(tid),
               'price': robin_stocks.robinhood.stocks.get_latest_price(tid),
               'historical': robin_stocks.robinhood.stocks.get_stock_historicals(tid, span='3month'),
               'plot_div': plot_div,
               'layout': layout,
               'order_form': order_form,
               }
    return render(request, 'account/ticker.html', context)
