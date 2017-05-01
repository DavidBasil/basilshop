from django.conf.urls import url
from . import views


urlpatterns = [
    # create order
    url(r'^create/$', views.order_create, name='order_create'),
]
