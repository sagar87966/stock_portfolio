from django import forms
from .models import AddStocks

class StockForm(forms.ModelForm):
    class Meta:
        model = AddStocks
        fields = ['ticker']