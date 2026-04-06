from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard:home')
    return render(request, 'dashboard/productForm.html', {'form':form})

