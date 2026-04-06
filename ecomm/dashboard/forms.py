from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user']

        widgets = {
        'product_name': forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-2 py-1.5 text-sm focus:ring-1 focus:ring-violet-500 focus:border-violet-500'
        }),
        'product_price': forms.NumberInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-2 py-1.5 text-sm focus:ring-1 focus:ring-violet-500 focus:border-violet-500'
        }),
        'product_brand': forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-2 py-1.5 text-sm focus:ring-1 focus:ring-violet-500 focus:border-violet-500'
        }),
        'product_qty': forms.NumberInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-2 py-1.5 text-sm focus:ring-1 focus:ring-violet-500 focus:border-violet-500'
        }),
        'product_describ': forms.Textarea(attrs={
            'class': 'w-full border border-gray-300 rounded px-2 py-1.5 text-sm focus:ring-1 focus:ring-violet-500 focus:border-violet-500',
            'rows': 2
        }),
        'product_image': forms.ClearableFileInput(attrs={
            'class': 'block w-full text-sm text-gray-600'
        }),
        }