from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings

from .serializers import UserDetailSerializer, SmsSerializer, UserRegisterSerializer
from .models import VerifyCode
from utils.sms import send_mobile_code, generate_code

User = get_user_model()


class UsersViewset(GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    '''
    retrieve:
        获取用户详细信息
    update:
        更新用户信息
    partial_update:
        更新用户信息(部分更新)
    '''
    queryset = User.objects.all()
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        return UserDetailSerializer

    def get_permissions(self):
        if self.action == "create":
            return []
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        re_dict = serializer.data
        re_dict["token"] = token
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        password = serializer.validated_data["password"]
        serializer.validated_data["password"] = make_password(password)
        return serializer.save()


class SmsCodeViewset(GenericViewSet, mixins.CreateModelMixin):
    '''
    create:
        发送短信验证码
    '''
    serializer_class = SmsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        code = generate_code()
        sms_status = send_mobile_code(mobile, code)

        if sms_status["status"] == "error":
            return Response({"mobile": sms_status["msg"]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            VerifyCode.objects.create(code=code, mobile=mobile)
            return Response({"mobile": mobile}, status=status.HTTP_201_CREATED)
