from django.urls import path
from . import views
app_name = 'user_dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('addproduct/', views.add_product, name='addproduct'),
    path('detail/<int:id>/', views.detailed_product, name='detailView'),
    path('updateproduct/<int:id>/', views.update_product, name='updateProduct'),
    path('deleteproduct/<int:id>/', views.delete_product, name='deleteProduct'),

    #API URL
    path('productapi/', views.product_api, name='product_api'),
    path('productapi/<int:pk>/', views.product_api_get, name='product_api_get'),
]
