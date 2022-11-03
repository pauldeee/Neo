import robin_stocks
import requests


# get the first stock returned by a search
def get_stocks_data(ticker):
    return robin_stocks.robinhood.stocks.find_instrument_data(ticker)[0]


def get_my_account():
    print(robin_stocks.robinhood.profiles.load_account_profile())
    return robin_stocks.robinhood.profiles.load_account_profile()
