from django.contrib.auth.models import User 
from .models import Order
from django import forms


class CheckOutForms(forms.ModelForm):
    
    class Meta:
        
        model = Order
        
        exclude = ["buyer", "seller", "order_number", "status", "order_total"]
        
    def __init__(self, *args, **kwargs):
        super(CheckOutForms, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})