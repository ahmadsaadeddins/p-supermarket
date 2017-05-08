from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /products/
    url(r'^$', views.index, name='index'),
    # ex: /products/1
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
]
