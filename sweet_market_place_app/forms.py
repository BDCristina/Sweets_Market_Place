# În forms.py

from django import forms
from .models import Mesaj, OrderItem


class MesajForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ['nume', 'prenume', 'email', 'phone', 'mesaj']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'

