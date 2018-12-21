"""rest_framework_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
import xadmin

from goods.viewset import GoodsViewset, CategoryViewset, HotSearchViewset, BannerViewset
from users.viewset import UsersViewset, SmsCodeViewset
from operation.viewset import UserFavViewset, LeavingMessageViewset, UserAddressViewset
from trade.viewset import ShopCartViewset, OrderViewset
from .settings import MEDIA_ROOT

router = routers.DefaultRouter()
router.register(r"goods_set", GoodsViewset, base_name="goods")
router.register(r"category_set", CategoryViewset, base_name="category")
router.register(r"hotSearch_set", HotSearchViewset, base_name="hotSearch")
router.register(r"banner_set", BannerViewset, base_name="banner")
router.register(r"users_set", UsersViewset, base_name="users")
router.register(r'smscode_set', SmsCodeViewset, base_name="smscode")
router.register(r'fav_set', UserFavViewset, base_name="fav")
router.register(r'message_set', LeavingMessageViewset, base_name="message")
router.register(r'address_set', UserAddressViewset, base_name="address")
router.register(r'shopcart_set', ShopCartViewset, base_name="shopcart")
router.register(r'order_set', OrderViewset, base_name="order")
# router.register(r"test_set", GoodsViewset, base_name="test_set")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^', include(router.urls)),
    url(r'^goods/', include("goods.urls")),
    url(r'^users/', include("users.urls")),
    url(r'^operation/', include("operation.urls")),
    url(r'^trade/', include("trade.urls")),

    url(r'^docs/', include_docs_urls(title="MxShop")),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
