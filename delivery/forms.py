from django import forms
from .models import Order as ModelOrder

class Order(forms.ModelForm):

    class Meta():
        model = ModelOrder
        fields = ['customer', 'value', 'product', 'address']
