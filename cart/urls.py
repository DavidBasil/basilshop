from django.conf.urls import url
from . import views


urlpatterns = [
    # cart's detailed view
    url(r'^$', views.cart_detail, name='cart_detail'),
    # add products to the cart
    url(r'^add/(?P<product_id>\d+)/$', 
        views.cart_add, 
        name='cart_add'),
    # remove product from the cart
    url(r'^remove/(?P<product_id>\d+)/$', 
        views.cart_remove, 
        name='cart_remove'),
]
