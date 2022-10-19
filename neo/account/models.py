from datetime import datetime
from decimal import Decimal

import pytz as pytz
from django.db import models


# Create your models here.

class Timeframes(models.TextChoices):
    MIN_1 = "1m"
    HOUR_1 = "1h"
    DAY_1 = "1d"


class Exchanges(models.TextChoices):
    COINBASE = 'coinbase'
    KRAKEN = 'kraken'
    ROBINHOOD = 'robinhood'


class Account(models.Model):
    # api for accessing account
    exchange = models.CharField(max_length=255, choices=Exchanges.choices)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)



class TradingBot(models.Model):
    pass


class Order(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open'
        CLOSED = 'closed'
        CANCELED = 'canceled'
        EXPIRED = 'expired'
        REJECTED = 'rejected'
        NOT_MIN_NOTIONAL = 'not min notional'

    class Type(models.TextChoices):
        # maybe do stop loss?
        MARKET = 'market'
        LIMIT = 'limit'


class Backtesting(models.Model):
    pass


class Asset(models.Model):
    # This can be a stock or crypto
    name = models.CharField(max_length=255, blank=True, null=True)
    ticker = models.CharField(max_length=20)


class Market:
    pass


class OHLCV(models.Model):
    """

    OHLCV candles https://github.com/ccxt/ccxt/wiki/Manual#ohlcv-structure
    """

    market = models.ForeignKey(Market, on_delete=models.PROTECT)
    timeframe = models.CharField(max_length=10, choices=Timeframes.choices)
    timestamp = models.DateTimeField()
    open_price = models.DecimalField(max_digits=30, decimal_places=8)
    highest_price = models.DecimalField(max_digits=30, decimal_places=8)
    lowest_price = models.DecimalField(max_digits=30, decimal_places=8)
    closing_price = models.DecimalField(max_digits=30, decimal_places=8)
    volume = models.DecimalField(max_digits=30, decimal_places=8)

    @staticmethod
    def get_OHLCV(candle: List[float], timeframe: str, market: Market) -> OHLCV:
        """Get a OHLCV candle from a OHLCV request
        Arguments:
            candle {List[float]} -- candle list
            timeframe {Timeframes} -- timeframe from candle
            market {Market} -- market from candle
        Returns:
            OHLCV -- unsaved OHLCV candle
        """
        return OHLCV(
            market=market,
            timeframe=timeframe,
            timestamp=datetime.fromtimestamp(candle[0] / 1000, tz=pytz.timezone("UTC")),
            open_price=Decimal(candle[1]),
            highest_price=Decimal(candle[2]),
            lowest_price=Decimal(candle[3]),
            closing_price=Decimal(candle[4]),
            volume=Decimal(candle[5]),
        )


class TradingStrategy(models.TextChoices):
    USER_CUSTOM = "custom"
    NEO_TRADE_AND_SELECT = "neo_all"
    NEO_TRADE_ONLY = "neo_trade"
