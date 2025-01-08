from django import forms

class ExcelUploadForm(forms.Form):
    file = forms.FileField()

from django import forms
from .models import StockItem

class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['name', 'category', 'quantity', 'price', 'week1', 'week2', 'week3', 'week4', 'week5']

    # Optional: You can add custom validation or logic here if needed.
