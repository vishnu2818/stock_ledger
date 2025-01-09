from django import forms
from .models import StockItem


class ExcelUploadForm(forms.Form):
    file = forms.FileField()


class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['medicine', 'scope_quantity', 'available_quantity', 'net_consumed', 'week1', 'week2', 'week3', 'week4', 'week5']

    # Optional: You can add custom validation or logic here if needed.
