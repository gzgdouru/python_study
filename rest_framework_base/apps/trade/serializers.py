import random
from datetime import datetime

from rest_framework import serializers

from goods.models import Goods
from goods.serializers import GoodsSerializer
from .models import ShoppingCart, OrderGoods, OrderInfo


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ["goods", "nums"]


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label="数量", min_value=1, error_messages={
        "min_value": "商品数量不能小于一",
        "required": "请选择购买数量",
    })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods).first()
        if existed:
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        instance.save()
        return instance

        # old_record = ShoppingCart.objects.get(id=instance.id)
        # instance.nums = validated_data["nums"]
        # instance.save()
        #
        # nums = instance.nums - old_record.nums
        # goods = old_record.goods
        # goods.goods_num -= nums
        # goods.save()
        # return instance


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    order_sn = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    pay_status = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def generate_order_sn(self):
        order_sn = "{time_str}{user_id}{random_str}".format(time_str=datetime.now().strftime("%Y%m%d%H%M%S"),
                                                            user_id=self.context["request"].user.id,
                                                            random_str=random.randint(10, 99))
        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    goods = OrderGoodsSerializer(many=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = OrderInfo
        fields = "__all__"
