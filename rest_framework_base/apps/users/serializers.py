import re
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_base.settings import REGEX_MOBILE
from .models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(min_length=11, max_length=11, required=True, help_text="手机号码")

    def validate_mobile(self, mobile):
        if User.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError("手机号码已存在")

        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago, mobile=mobile).exists():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "gender", "birthday", "email", "mobile"]


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(min_length=6, max_length=6, required=True, write_only=True, label="验证码",
                                 help_text="验证码", error_messages={
            "blank": "请输入验证码",
            "required": "请输入验证码",
            "min_length": "验证码格式为6位数字",
            "max_length": "验证码格式为6位数字",
        })
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(User.objects.all(), message="用户名已存在")])
    password = serializers.CharField(style={"input_type": "password"}, help_text="密码", label="密码", write_only=True)

    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_code(self, code):
        verify_record = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time").first()
        if verify_record:
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minutes_ago > verify_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if verify_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ["username", "code", "mobile", "password"]
