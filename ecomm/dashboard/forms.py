from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Msta:
        model = Product
        fields = "__all__"