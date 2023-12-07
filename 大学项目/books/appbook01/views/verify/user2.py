from rest_framework.viewsets import ModelViewSet
from appbook01.models import UserInfo
from rest_framework import serializers


class PublishesSerializers(serializers.ModelSerializer):
    verificationCode = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserInfo
        fields = [f.name for f in UserInfo._meta.fields] + ["verificationCode"]

    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("用户名必须由字母和数字组成")
        # 检查用户名是否已存在
        if UserInfo.objects.filter(username=value).exists():
            raise serializers.ValidationError("用户名已被使用")
        return value

    def validate_verificationCode(self, value):
        """校验验证码"""
        session_code = self.context['request'].session.get('message_code')  # 获取session中的验证码
        if value != session_code:
            raise serializers.ValidationError("验证码不正确")
        return value

    def create(self, validated_data):
        # 从验证后的数据中移除verificationCode，因为它不应该保存到数据库中
        validated_data.pop('verificationCode', None)
        return super(PublishesSerializers, self).create(validated_data)


class User(ModelViewSet):
    queryset = UserInfo.objects
    serializer_class = PublishesSerializers

    def get_serializer_context(self):
        """Ensure that the serializer has access to the request object"""
        return {"request": self.request}
