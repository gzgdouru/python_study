from django.shortcuts import Http404
from django.db import transaction
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from .models import ShoppingCart, OrderInfo, OrderGoods
from .serializers import ShopCartSerializer, ShopCartDetailSerializer, OrderSerializer, OrderDetailSerializer
from utils.permissions import IsOwnerOrReadOnly


class ShopCartPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page"
    page_size_query_param = "page_size"


class ShopCartViewset(ModelViewSet):
    '''
    list:
        获取购物车详情
    create:
        加入购物车
    retrieve:
        查看购物车商品详情
    update:
        更新购物车
    destroy:
        移除购物车商品
    '''
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = ShopCartPagination
    lookup_field = "goods_id"

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ShopCartDetailSerializer
        return ShopCartSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            shopcart = serializer.save()
            goods = shopcart.goods
            nums = serializer.validated_data["nums"]
            goods.goods_num -= nums
            goods.save()

    def perform_update(self, serializer):
        with transaction.atomic():
            existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
            saved_record = serializer.save()
            diff_nums = saved_record.nums - existed_record.nums
            goods = saved_record.goods
            goods.goods_num -= diff_nums
            goods.save()

    def perform_destroy(self, instance):
        with transaction.atomic():
            goods = instance.goods
            goods.goods_num += instance.nums
            goods.save()
            instance.delete()


class OrderViewset(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):
    '''
    list:
        获取订单列表
    create:
        新建订单
    retrieve:
        获取订单详情
    '''
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            order = serializer.save()
            shop_carts = ShoppingCart.objects.filter(user=self.request.user)
            for shop_cart in shop_carts:
                order_goods = OrderGoods()
                order_goods.goods_num = shop_cart.nums
                order_goods.goods = shop_cart.goods
                order_goods.order = order
                order_goods.save()

                shop_cart.delete()
            return order
