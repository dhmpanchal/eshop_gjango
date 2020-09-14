from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products/')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_category(categoryId):
        return Product.objects.filter(category_id=categoryId)

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)