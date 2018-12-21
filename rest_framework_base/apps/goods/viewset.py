from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .serializers import GoodsSerializer, CategorySerializer, HotSearchSerializer, BannerSerializer
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    # django_paginator_class = LimitOffsetPagination
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"


class CategoryPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page"
    page_size_query_param = "page_size"


class GoodsViewset(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    '''
    list:
        获取商品列表
    retrieve:
        获取商品详情
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filter_fields = ('name',)
    filter_class = GoodsFilter
    search_fields = ["name"]
    ordering_fields = ["shop_price"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewset(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    '''
    list:
        获取分类商品列表
    retrieve:
        获取分类商品详情
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class HotSearchViewset(GenericViewSet, mixins.ListModelMixin):
    '''
    list:
        获取热搜词列表
    '''
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotSearchSerializer


class BannerViewset(GenericViewSet, mixins.ListModelMixin):
    '''
    list:
        获取轮播图列表
    '''
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer