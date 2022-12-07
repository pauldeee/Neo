import pandas as pd
import robin_stocks.robinhood.stocks
import robin_stocks.robinhood.stocks
from backtesting import Backtest, Strategy
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score


class SignalStrategy(Strategy):
    def init(self):
        pass

    def next(self):
        current_buy_signal = self.data.Buy[-1]

        if current_buy_signal == 1:
            if not self.position:
                self.buy()

        elif current_buy_signal == 0:
            if self.position:
                self.position.close()


class SingleStockTradingBot:
    def __init__(self, robin_user, robin_pass, ticker):
        self.robin_user = robin_user
        self.robin_pass = robin_pass
        self.ticker = ticker
        self.login()

    # login to robinhood -- sometimes needed, also used to ensure bot can place trades.
    def login(self):
        robin_stocks.robinhood.authentication.login(self.robin_user, self.robin_pass)

    # create a standard ohlcv df for computing ML stuff with stocks or crypto.
    @staticmethod
    def robin_historical_dict_to_ohlcv_df(robin_historicals: dict):
        df = pd.DataFrame.from_dict(robin_historicals)
        df.drop(columns=['session', 'interpolated', 'symbol'], axis=1, inplace=True)
        df.rename(columns={"begins_at": "date", "open_price": "open", "close_price": "close", "high_price": "high",
                           "low_price": "low"}, inplace=True)
        df['open'] = pd.to_numeric(df['open'])
        df['high'] = pd.to_numeric(df['high'])
        df['low'] = pd.to_numeric(df['low'])
        df['close'] = pd.to_numeric(df['close'])
        df['volume'] = pd.to_numeric(df['volume'])
        df = df[['date', 'open', 'high', 'low', 'close', 'volume']]  # reorder to match OHLCV
        df.set_index('date', inplace=True)
        return df

    @staticmethod
    def backtest(data, model, predictors, start=365, step=90, probability=0.6):
        predictions = []
        # Loop over the dataset in increments
        for i in range(start, data.shape[0], step):
            # Split into train and test sets
            train = data.iloc[0:i].copy()
            test = data.iloc[i:(i + step)].copy()

            # Fit the random forest model
            model.fit(train[predictors], train["target"])

            # Make predictions
            preds = model.predict_proba(test[predictors])[:, 1]
            preds = pd.Series(preds, index=test.index)
            preds[preds > probability] = 1
            preds[preds <= probability] = 0

            # Combine predictions and test values
            combined = pd.concat({"target": test["target"], "predictions": preds}, axis=1)

            predictions.append(combined)

        return pd.concat(predictions)

    # This method takes a ticker then using ML ForestClassifier returns if a prediction says it should buy the stock,
    # the stock ticker, and precision score of the ML result the method inspired by code found here:
    # https://www.dataquest.io/blog/portfolio-project-predicting-stock-prices-using-pandas-and-scikit-learn/
    def create_predictions_for_stock_with_signals(self):
        try:
            self.login()
            hist = self.robin_historical_dict_to_ohlcv_df(
                robin_stocks.robinhood.stocks.get_stock_historicals(self.ticker, interval='day', span='5year'))

            data = hist[["close"]]
            data = data.rename(columns={"close": "actual_close"})
            # print(data.head())

            # find if close is higher or lower than the day before
            data["target"] = hist.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])["close"]

            # shift prices to predict tomorrow's price
            hist_prev = hist.copy()
            hist_prev = hist_prev.shift(1)
            # print(hist_prev.head())

            # data for prediction
            predictors = ["open", "high", "low", "close", "volume"]
            data = data.join(hist_prev[predictors]).iloc[1:]

            # create the model
            model = RandomForestClassifier(n_estimators=50, min_samples_split=200, random_state=1)

            # means
            weekly_mean = data.rolling(7).mean()['close']
            monthly_mean = data.rolling(30).mean()['close']
            quarterly_mean = data.rolling(90).mean()['close']
            annual_mean = data.rolling(365).mean()['close']

            # trend
            weekly_trend = data.shift(1).rolling(7).sum()['target']
            monthly_trend = data.shift(1).rolling(30).sum()['target']
            quarterly_trend = data.shift(1).rolling(90).sum()['target']
            annual_trend = data.shift(1).rolling(365).sum()['target']

            # add means to df
            data["weekly_mean"] = weekly_mean / data["close"]
            data["monthly_mean"] = monthly_mean / data["close"]
            data["quarterly_mean"] = quarterly_mean / data["close"]
            data["annual_mean"] = annual_mean / data["close"]

            data["annual_weekly_mean"] = data["annual_mean"] / data["weekly_mean"]
            data["annual_quarterly_mean"] = data["annual_mean"] / data["quarterly_mean"]

            # add trends to df
            data["weekly_trend"] = weekly_trend
            data["monthly_trend"] = monthly_trend
            data["quarterly_trend"] = quarterly_trend
            data["annual_trend"] = annual_trend

            # add some ratios
            data["open_close_ratio"] = data["open"] / data["close"]
            data["high_close_ratio"] = data["high"] / data["close"]
            data["low_close_ratio"] = data["low"] / data["close"]

            # moving average increasing
            # something where 1 says MA is upward

            # moving average decreasing
            # something like 0 means MA is downward

            # update predictors
            full_predictors = predictors + [
                'weekly_mean',
                'monthly_mean',
                'quarterly_mean',
                'annual_mean',
                'annual_weekly_mean',
                'annual_quarterly_mean',
                'open_close_ratio',
                'high_close_ratio',
                'weekly_trend',
                'monthly_trend',
                'quarterly_trend',
                'annual_trend',
                'low_close_ratio'
            ]

            predictions = self.backtest(data.iloc[365:], model, full_predictors)
            # return ticker, precision_score(predictions['target'], predictions['predictions'], zero_division=0) * 100, \
            #        predictions['predictions'][-1]

            combined = pd.concat([predictions, data], axis=1)
            combined.dropna(inplace=True)
            combined["buy"] = combined["predictions"]

            sell = combined[['buy']].copy()
            sell = sell.rename(columns={'buy': 'sell'})
            sell = sell.shift(1)

            combined = pd.concat([combined, sell], axis=1)
            combined.dropna(inplace=True)
            combined = combined.rename(
                columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume',
                         'buy': 'Buy',
                         'sell': 'Sell'})
            combined['Buy'] = pd.to_numeric(combined['Buy'])
            combined['Sell'] = pd.to_numeric(combined['Sell'])
            combined.drop(
                columns=[
                    # 'target', 'predictions', 'target', 'actual_close',
                    'weekly_mean', 'monthly_mean', 'quarterly_mean',
                    'annual_mean', 'annual_weekly_mean', 'high_close_ratio', 'low_close_ratio',
                    'annual_quarterly_mean', 'weekly_trend', 'monthly_trend', 'quarterly_trend',
                    'annual_trend', 'open_close_ratio'
                ],
                inplace=True)

            combined.index = pd.to_datetime(combined.index)

            return combined
        except:
            return None

    def run_once(self):
        try:
            bot = SingleStockTradingBot(self.robin_user, self.robin_pass, self.ticker)
            result_data = bot.create_predictions_for_stock_with_signals()
            bt = Backtest(result_data, SignalStrategy, cash=10_000, trade_on_close=True)
            return bt.run()
        except:
            return None


class StockMarketWideTradingBot:
    def __init__(self, robin_user, robin_pass):
        self.robin_user = robin_user
        self.robin_pass = robin_pass
        self.login()
        self.isTrading = True
        # self.thread = Thread(target=self.__trading_bot())
        # self.thread.start()

    def login(self):
        robin_stocks.robinhood.authentication.login(self.robin_user, self.robin_pass)

    # create a standard ohlcv df for computing ML stuff with stocks or crypto.
    @staticmethod
    def robin_historical_dict_to_ohlcv_df(robin_historicals: dict):
        df = pd.DataFrame.from_dict(robin_historicals)
        df.drop(columns=['session', 'interpolated', 'symbol'], axis=1, inplace=True)
        df.rename(columns={"begins_at": "date", "open_price": "open", "close_price": "close", "high_price": "high",
                           "low_price": "low"}, inplace=True)
        df['open'] = pd.to_numeric(df['open'])
        df['high'] = pd.to_numeric(df['high'])
        df['low'] = pd.to_numeric(df['low'])
        df['close'] = pd.to_numeric(df['close'])
        df['volume'] = pd.to_numeric(df['volume'])
        df = df[['date', 'open', 'high', 'low', 'close', 'volume']]  # reorder to match OHLCV
        df.set_index('date', inplace=True)

        return df

    @staticmethod
    def backtest(data, model, predictors, start=365, step=90, probability=0.6):
        predictions = []
        # Loop over the dataset in increments
        for i in range(start, data.shape[0], step):
            # Split into train and test sets
            train = data.iloc[0:i].copy()
            test = data.iloc[i:(i + step)].copy()

            # Fit the random forest model
            model.fit(train[predictors], train["target"])

            # Make predictions
            preds = model.predict_proba(test[predictors])[:, 1]
            preds = pd.Series(preds, index=test.index)
            preds[preds > probability] = 1
            preds[preds <= probability] = 0

            # Combine predictions and test values
            combined = pd.concat({"target": test["target"], "predictions": preds}, axis=1)

            predictions.append(combined)

        return pd.concat(predictions)

    # this method creates a list of stock tickers for which we should explore trading
    @staticmethod
    def create_stock_list():
        upcoming_earnings = robin_stocks.robinhood.get_all_stocks_from_market_tag('upcoming-earnings')
        tech = robin_stocks.robinhood.get_all_stocks_from_market_tag('technology')
        bio = robin_stocks.robinhood.get_all_stocks_from_market_tag('biopharmaceutical')
        most_pop_under_25 = robin_stocks.robinhood.get_all_stocks_from_market_tag('most-popular-under-25')
        top_100 = robin_stocks.robinhood.get_all_stocks_from_market_tag('100-most-popular')
        energy = robin_stocks.robinhood.get_all_stocks_from_market_tag('energy')
        banks = robin_stocks.robinhood.get_all_stocks_from_market_tag('banking')

        stocks = upcoming_earnings
        stocks += tech
        stocks += bio
        stocks += most_pop_under_25
        stocks += top_100
        stocks += energy
        stocks += banks

        # CLEAN STOCKS
        # remove duplicate stocks
        stocks = [i for n, i in enumerate(stocks) if i not in stocks[:n]]

        # remove stocks that cannot be traded
        for s in stocks:
            if s['trading_halted'] == 'True' or s['state'] != 'active':
                stocks.remove(s)
        print(len(stocks))

        return stocks

    # This method takes a ticker then using ML ForestClassifier returns if a prediction says it should buy the stock,
    # the stock ticker, and precision score of the ML result
    # the method inspired by code found here: https://www.dataquest.io/blog/portfolio-project-predicting-stock-prices-using-pandas-and-scikit-learn/
    def create_predictions_for_stock(self, ticker):
        try:
            ruser, rpass = 'paulduzynski@protonmail.com', 'Pduz304491!'
            robin_stocks.robinhood.authentication.login(ruser, rpass)

            hist = self.robin_historical_dict_to_ohlcv_df(
                robin_stocks.robinhood.stocks.get_stock_historicals(ticker, interval='day', span='5year'))

            data = hist[["close"]]
            data = data.rename(columns={"close": "actual_close"})
            # print(data.head())

            # find if close is higher or lower than the day before
            data["target"] = hist.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])["close"]

            # shift prices to predict tomorrow's price
            hist_prev = hist.copy()
            hist_prev = hist_prev.shift(1)
            # print(hist_prev.head())

            # data for prediction
            predictors = ["open", "high", "low", "close", "volume"]
            data = data.join(hist_prev[predictors]).iloc[1:]

            # create the model
            model = RandomForestClassifier(n_estimators=50, min_samples_split=200, random_state=1)

            # means
            weekly_mean = data.rolling(7).mean()['close']
            monthly_mean = data.rolling(30).mean()['close']
            quarterly_mean = data.rolling(90).mean()['close']
            annual_mean = data.rolling(365).mean()['close']

            # trend
            weekly_trend = data.shift(1).rolling(7).sum()['target']
            monthly_trend = data.shift(1).rolling(30).sum()['target']
            quarterly_trend = data.shift(1).rolling(90).sum()['target']
            annual_trend = data.shift(1).rolling(365).sum()['target']

            # add means to df
            data["weekly_mean"] = weekly_mean / data["close"]
            data["monthly_mean"] = monthly_mean / data["close"]
            data["quarterly_mean"] = quarterly_mean / data["close"]
            data["annual_mean"] = annual_mean / data["close"]

            data["annual_weekly_mean"] = data["annual_mean"] / data["weekly_mean"]
            data["annual_quarterly_mean"] = data["annual_mean"] / data["quarterly_mean"]

            # add trends to df
            data["weekly_trend"] = weekly_trend
            data["monthly_trend"] = monthly_trend
            data["quarterly_trend"] = quarterly_trend
            data["annual_trend"] = annual_trend

            # add some ratios
            data["open_close_ratio"] = data["open"] / data["close"]
            data["high_close_ratio"] = data["high"] / data["close"]
            data["low_close_ratio"] = data["low"] / data["close"]

            # moving average increasing
            # something where 1 says MA is upward

            # moving average decreasing
            # something like 0 means MA is downward

            # update predictors
            full_predictors = predictors + [
                'weekly_mean',
                'monthly_mean',
                'quarterly_mean',
                'annual_mean',
                'annual_weekly_mean',
                'annual_quarterly_mean',
                'open_close_ratio',
                'high_close_ratio',
                'weekly_trend',
                'monthly_trend',
                'quarterly_trend',
                'annual_trend',
                'low_close_ratio'
            ]

            predictions = self.backtest(data.iloc[365:], model, full_predictors)

            return ticker, precision_score(predictions['target'], predictions['predictions'], zero_division=0) * 100, \
                   predictions['predictions'][-1]
        except:
            return ticker, 0, 0  # in this case, the ML has failed,probably a data / not enough data issue?? Look
            # into this if have time

    def find_stocks_to_buy(self):
        # get a list of stocks
        stocks = self.create_stock_list()

        # create prediction on each stock
        pred_tups = []
        for s in stocks:
            pred_tups.append(self.create_predictions_for_stock(s['symbol']))

        print(pred_tups)

        # only keep the buy predictions

        final_preds = []
        for tup in pred_tups:
            if int(tup[1]) != 0.0 and int(tup[2]) != 0:
                final_preds.append(tup)

            # now sort by highest probability of success
            # final_preds = pred_tups.sort(key=lambda x: x[1])
        final_preds = sorted(final_preds, key=lambda t: t[1], reverse=True)

        print(final_preds)

        # now take the top 10 stocks with the highest probability and a buy signal
        stocks_to_buy = []
        counter = 0
        for i in range(len(final_preds)):
            if counter < 10 and final_preds[i][1] >= 50:
                stocks_to_buy.append(final_preds[i])
                counter += 1

        return stocks_to_buy

    # this method takes a list of tuple with a ticker in position 0 of the tuple and buys the asset
    def place_buy_orders(self, stocks_to_buy: list):
        # get available cash
        profile = robin_stocks.robinhood.profiles.load_account_profile()
        buying_power = profile['buying_power']
        # Only use 1% of available cash on each buy order
        dollars_for_trade = float(buying_power) * 0.01
        for stock in stocks_to_buy:
            robin_stocks.robinhood.orders.order_buy_fractional_by_price(stock[0], dollars_for_trade)
            print('buying stock: ', stock[0], '\tamount: ', str(dollars_for_trade))

    # this places sell orders for all stocks. this is used at the end of the trading day before close.
    def sell_all_stocks(self):
        self.login()
        # get portfolio holdings
        holdings = robin_stocks.robinhood.account.build_holdings()
        # sell all stocks that are currently held
        for key in holdings:
            robin_stocks.robinhood.orders.order_sell_fractional_by_quantity(key, holdings[key]['quantity'])

    # this method runs the bot ONCE. This should be spun in a thread for continuous bot operation
    def run_once(self):
        self.login()
        stocks_to_buy = self.find_stocks_to_buy()
        self.place_buy_orders(stocks_to_buy)
        self.sell_all_stocks()

    # this runs the bot in a new thread
    def start_trading_bot(self):
        print("starting the bot")
        self.thread.start()
        return True

    # this stops trading bot, places orders to sell, and cancels open orders if any
    def stop_bot_sell_all_cancel_all(self):
        self.login()
        print("cancelling all orders")
        robin_stocks.robinhood.cancel_all_stock_orders()
        print("selling all stocks")
        self.sell_all_stocks()

    def cancel_all(self):
        self.login()
        print("cancelling all orders")
        robin_stocks.robinhood.cancel_all_stock_orders()
