from django_filters.rest_framework import FilterSet
from django_filters import CharFilter, NumberFilter
from django.db.models import Q

from .models import Goods


class GoodsFilter(FilterSet):
    name = CharFilter(field_name="name", help_text="商品名称", lookup_expr='icontains')
    min_price = NumberFilter(field_name="shop_price", help_text="商品最低价格", lookup_expr="gte")
    max_price = NumberFilter(field_name="shop_price", help_text="商品最高价格", lookup_expr="lte")
    top_category = NumberFilter(method="top_category_filter", help_text="分类id", label="分类id")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ["name", "min_price", "max_price", 'is_hot', 'is_new', "top_category"]
