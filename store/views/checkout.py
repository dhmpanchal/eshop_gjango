from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        uid = request.session.get('uid')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))

        for product in products:
            order = Order(product_id=product.id,
                        user_id=uid,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)),
                        price=product.price)
            order.create_order()
        request.session['cart'] = {}
        return redirect('cart')
    