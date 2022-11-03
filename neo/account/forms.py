from django import forms


# TickerForm example from this video series https://www.youtube.com/watch?v=Ozv_9tEe7Cw
class TickerForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=64)
