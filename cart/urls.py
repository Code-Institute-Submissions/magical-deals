from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, empty_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<pk>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<pk>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^empty_cart/$', empty_cart, name='empty_cart'),
]
