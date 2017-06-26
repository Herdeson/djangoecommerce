
from django.conf.urls import url

from . import views


# url primeiro padrao, segundo a view, nome para ser utilizado nos templates
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'), #url amigavel parametrizada
    url(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'), #url amigavel parametrizada
]
