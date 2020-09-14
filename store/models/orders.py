from django.db import models
import datetime
from .product import Product
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    quantity = models.IntegerField(default=1)
    price  = models.IntegerField(default=0)
    order_date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def create_order(self):
        return self.save()

    @staticmethod
    def get_orders_by_user(uid):
        return Order.objects.filter(user=uid).order_by('-order_date')