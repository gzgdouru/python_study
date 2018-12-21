from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .serializers import GoodsSerializer, CategorySerializer, HotSearchSerializer, BannerSerializer


class GoodsListView(generics.ListAPIView):
    '''获取商品列表页'''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = LimitOffsetPagination


class GoodDetailView(generics.RetrieveAPIView):
    '''获取商品详情'''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryListView(generics.ListAPIView):
    '''获取商品分类列表'''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination


class CategoryDetailView(generics.RetrieveAPIView):
    '''获取商品分类详情'''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchListView(generics.ListAPIView):
    '''获取热搜词列表'''
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotSearchSerializer


class BannerListView(generics.ListAPIView):
    '''获取轮播图列表'''
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
