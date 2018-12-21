from django.db import transaction
from rest_framework import generics
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


class ShopCartListView(generics.ListAPIView):
    '''获取购物车详情'''
    # queryset = ShoppingCart.objects.all()
    serializer_class = ShopCartDetailSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = ShopCartPagination

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class ShopCartCreateView(generics.CreateAPIView):
    '''加入购物车'''
    serializer_class = ShopCartSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        with transaction.atomic():
            shopcart = serializer.save()
            goods = shopcart.goods
            nums = serializer.validated_data["nums"]
            goods.goods_num -= nums
            goods.save()


class ShopCartDetailView(generics.RetrieveAPIView):
    '''查看购物车商品详情'''
    serializer_class = ShopCartDetailSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "goods_id"

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class ShopCartUpdateView(generics.UpdateAPIView):
    '''更新购物车'''
    serializer_class = ShopCartSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "goods_id"

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        with transaction.atomic():
            old_record = ShoppingCart.objects.get(id=serializer.instance.id)
            shop_cart = serializer.save()
            diff_nums = shop_cart.nums - old_record.nums
            goods = shop_cart.goods
            goods.goods_num -= diff_nums
            goods.save()


class ShopCartRemoveView(generics.DestroyAPIView):
    '''移除购物车商品'''
    serializer_class = ShopCartSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "goods_id"

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        goods = instance.goods
        goods.goods_num += instance.nums
        goods.save()
        instance.delete()


class OrderListView(generics.ListAPIView):
    '''获取用户订单列表'''
    serializer_class = OrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)


class OrderCreateView(generics.CreateAPIView):
    '''创建用户订单'''
    serializer_class = OrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

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


class OrderDetailView(generics.RetrieveAPIView):
    '''获取用户订单详情'''
    serializer_class = OrderDetailSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)


class OrderRemoveView(generics.DestroyAPIView):
    '''删除订单'''
    serializer_class = OrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)
