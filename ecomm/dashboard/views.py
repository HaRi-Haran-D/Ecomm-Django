from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer

# Create your views here.

#API Function
@api_view(["GET", "POST"])
def product_api(request):
    if request.method =="GET":
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(["GET"])
def product_api_get(request,pk):
    product = Product.objects.get(pk=pk)
    serialier = ProductSerializer(product)
    return Response(serialier.data)



#No Function
def home(request):
    list = Product.objects.all()
    paginator = Paginator(list,2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/home.html', {'page_obj':page_obj})


def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        messages.success(request, "A product has been added")
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