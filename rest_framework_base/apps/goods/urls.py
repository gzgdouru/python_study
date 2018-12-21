from django.conf.urls import url

from . import views

app_name = "goods"

urlpatterns = [
    url(r'^$', views.GoodsListView.as_view(), name="goods_list"),
    url(r'^(?P<pk>\d+)/$', views.GoodDetailView.as_view(), name="goods_detail"),
    url(r'^category/$', views.CategoryListView.as_view(), name="category_list"),
    url(r'^category/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name="category_detail"),
    url(r'^hotSearch/$', views.HotSearchListView.as_view(), name="hotSearch_list"),
    url(r'^banner/$', views.BannerListView.as_view(), name="banner_list"),
]
