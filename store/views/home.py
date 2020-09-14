from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category

class Home(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categoryId = request.GET.get('cat_id')
        if categoryId:
            products = Product.get_products_by_category(categoryId)
        else:
            products = Product.get_all_products()
        categories = Category.get_all_categories()
        data = {
            'products': products,
            'categories': categories
            }
        return render(request, 'index.html', data)

    def post(self, request):
        pid = request.POST.get("pid")
        remove = request.POST.get("remove")
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pid)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(pid)
                    else:
                        cart[pid] = quantity - 1
                else:        
                    cart[pid] = quantity + 1
            else:
                cart[pid] = 1
        else:
            cart = {}
            cart[pid] = 1
        request.session['cart'] = cart
        print("----------->", request.session['cart'])
        return redirect("index")