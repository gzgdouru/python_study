from django.conf.urls import url

from . import views

app_name = "trade"

urlpatterns = [
    url(r'^shopcart/$', views.ShopCartListView.as_view(), name="shopcart_list"),
    url(r'^shopcart/create/$', views.ShopCartCreateView.as_view(), name="shopcart_create"),
    url(r'shopcart/(?P<goods_id>\d+)/$', views.ShopCartDetailView.as_view(), name="shopcart_detail"),
    url(r'shopcart/update/(?P<goods_id>\d+)/$', views.ShopCartUpdateView.as_view(), name="shopcart_update"),
    url(r'shopcart/remove/(?P<goods_id>\d+)/$', views.ShopCartRemoveView.as_view(), name="shopcart_remove"),
    url(r'^order/$', views.OrderListView.as_view(), name="order_list"),
    url(r'^order/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name="order_detail"),
    url(r'^order/create/$', views.OrderCreateView.as_view(), name="order_create"),
    url(r'^order/remove/(?P<pk>\d+)/$', views.OrderRemoveView.as_view(), name="order_remove"),
]
