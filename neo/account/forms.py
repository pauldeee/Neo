from django import forms


class OrderForm(forms.Form):
    pass


# TickerForm example from this video series https://www.youtube.com/watch?v=Ozv_9tEe7Cw
class BuyOrderForm(forms.Form):
    TRADE_CHOICES = (
        ('buy', 'BUY'),
        ('sell', 'SELL')
    )
    # trade = forms.ChoiceField(label='Trade', choices=TRADE_CHOICES)
    # ticker = forms.CharField(label='Ticker', max_length=32)
    amount_to_buy = forms.CharField(label='Amount to BUY', max_length=32)
    # price = forms.CharField(label='Price', max_length=32)


class SellOrderForm(forms.Form):
    amount_to_sell = forms.CharField(label='Amount to SELL', max_length=32)
