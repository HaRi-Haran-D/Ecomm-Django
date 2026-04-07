from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    list = Product.objects.all()
    return render(request, 'dashboard/home.html', {'list':list})


def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('dashboard:home')
    return render(request, 'dashboard/productForm.html', {'form':form})


def detailed_product(request, id):
    item = Product.objects.get(id=id)
    return render(request, 'dashboard/detailView.html', {'item':item})