from django.conf.urls import url
from . import views


urlpatterns = [
    # view with PayPal form with the 'Buy Now' button
    url(r'^process/$', views.payment_process, name='process'),
    # after the payment was successful
    url(r'^done/$', views.payment_done, name='done'),
    # canceled payment
    url(r'^canceled/$', views.payment_canceled, name='canceled'),
]
