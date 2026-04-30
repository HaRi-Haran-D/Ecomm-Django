from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_describ = models.TextField()
    product_image = models.ImageField(default='default.png', upload_to='products')
    product_brand = models.CharField(max_length=100)
    product_qty = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name

# class ProductImage(models.Model):
#     image = models.OneToManyField(Product, on_delete=models.CASCADE)
