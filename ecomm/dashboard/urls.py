from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('addproduct/', views.add_product, name='addproduct'),
    path('detail/<int:id>/', views.detailed_product, name='detailView'),
]
