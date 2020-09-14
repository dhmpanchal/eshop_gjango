from django.views import View
from django.shortcuts import render, redirect
from store.models.orders import Order


class OrderView(View):
    
    def get(self, request):
        uid = request.session.get('uid')
        orders = Order.get_orders_by_user(uid)
        return render(request, 'orders.html', {'orders': orders})