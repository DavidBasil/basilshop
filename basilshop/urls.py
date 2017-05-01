from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),
    # cart
    url(r'^cart/', include('cart.urls', namespace='cart')),
    # paypal
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # payment
    url(r'^payment/', include('payment.urls', namespace='payment')),
    # homepage
    url(r'^', include('shop.urls', namespace='shop')),
    # orders
    url(r'^orders/', include('orders.urls', namespace='orders')),
]
