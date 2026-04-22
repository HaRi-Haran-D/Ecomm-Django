from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
        # messages.success(request, "")
        return redirect('user_dashboard:home')
    return render(request, 'dashboard/productForm.html', {'form':form})


def detailed_product(request, id):
    item = Product.objects.get(id=id)
    return render(request, 'dashboard/detailView.html', {'item':item})


def update_product(request, id):
    item = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('user_dashboard:home')
    return render(request, 'dashboard/updateForm.html', {'form':form})


def delete_product(request, id):
    item = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('user_dashboard:home')
    return redirect('dashboard:detailView')