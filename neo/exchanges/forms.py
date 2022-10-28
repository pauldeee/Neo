from django import forms
from .models import Exchange


# class ExchangeForm(forms.ModelForm):
#     class Meta:
#         model = Exchange
#         fields = ('exchange', 'api_key, api_secret')
#         widgets = {
#             'exchange': forms.Select(),
#             'api_key': forms.TextInput,
#             'api_secret': forms.TextInput
#         }
