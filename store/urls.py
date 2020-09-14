from django.urls import path
from .views.home import Home
from .views.signup import SignUp
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('signup', SignUp.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', Checkout.as_view(), name="checkout"),
    path('orders', auth_middleware(OrderView.as_view()), name="orders"),
]