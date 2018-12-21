from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .models import UserFav, UserLeavingMessage, UserAddress
from .serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, AddressSerializer
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewset(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    '''
    list:
        获取用户收藏列表
    create:
        新增用户收藏商品
    retrieve:
        判断某个商品是否已经收藏
    destroy:
        删除用户收藏商品
    '''
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return UserFavDetailSerializer
        return UserFavSerializer


class LeavingMessageViewset(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    '''
    list:
        获取用户留言列表
    create:
        新增用户留言
    destroy:
        删除用户留言
    '''
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination
    serializer_class = LeavingMessageSerializer

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class UserAddressViewset(ModelViewSet):
    '''
    list:
        获取用户收货地址列表
    create:
        添加用户收货地址
    retrieve:
        获取用户收货地址详细信息
    update:
        更新用户收货地址
    destroy:
        删除用户收货地址
    '''
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
