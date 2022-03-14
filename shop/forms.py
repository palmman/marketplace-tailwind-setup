from django import forms
from django.contrib.auth.models import User 
from .models import Product

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        
class AddProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        exclude = ["seller", "slug"]
        
    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})