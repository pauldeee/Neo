from django import forms


# TickerForm example from this video series https://www.youtube.com/watch?v=Ozv_9tEe7Cw
class OrderForm(forms.Form):
    TRADE_CHOICES = (
        ('buy', 'BUY'),
        ('sell', 'SELL')
    )
    trade = forms.ChoiceField(label='Trade', choices=TRADE_CHOICES)
    # ticker = forms.CharField(label='Ticker', max_length=32)
    amount = forms.CharField(label='Amount ', max_length=32)
    # price = forms.CharField(label='Price', max_length=32)
