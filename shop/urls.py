from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    # homepage
    url(r'^$', views.product_list, name='product_list'),
    # category view
    url(r'^(?P<category_slug>[-\w]+)/$', 
        views.product_list, 
        name='product_list_by_category'),
    # particular product view
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 
        views.product_detail,
        name='product_detail'),
]


# static folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
