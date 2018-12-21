from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .models import UserFav, UserLeavingMessage, UserAddress
from .serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, AddressSerializer
from utils.permissions import IsOwnerOrReadOnly


class UserFavListView(generics.ListCreateAPIView):
    '''
    list:
        获取用户收藏商品列表
    create:
        新增用户收藏商品
    '''
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request and self.request.method == "POST":
            return UserFavDetailSerializer
        return UserFavSerializer


class UserFavDetailView(generics.RetrieveDestroyAPIView):
    '''
    retrieve:
        判断某个商品是否已经收藏
    destroy:
        移除用户收藏商品
    '''
    serializer_class = UserFavSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)


class LeavingMessageListView(generics.ListAPIView):
    '''获取用户留言'''
    serializer_class = LeavingMessageSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class LeavingMessageCreateView(generics.CreateAPIView):
    '''新增用户留言'''
    serializer_class = LeavingMessageSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class LeavingMessageRemoveView(generics.DestroyAPIView):
    '''删除用户留言'''
    serializer_class = LeavingMessageSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressListView(generics.ListAPIView):
    '''获取用户收货地址列表'''
    serializer_class = AddressSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class AddressCreateView(generics.CreateAPIView):
    '''添加用户收货地址'''
    serializer_class = AddressSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class AddressDetailView(generics.RetrieveAPIView):
    '''获取用户收货地址详细信息'''
    serializer_class = AddressSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class AddressUpdateView(generics.UpdateAPIView):
    '''更新用户收货地址'''
    serializer_class = AddressSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class AddressRemoveView(generics.DestroyAPIView):
    '''删除用户收货地址'''
    serializer_class = AddressSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
