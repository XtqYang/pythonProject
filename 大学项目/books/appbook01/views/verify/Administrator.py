from rest_framework.viewsets import ModelViewSet
from appbook01.models import Admin

from rest_framework import serializers

from appbook01.middleware.verify import CustomCookieAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


# 对于需要验证的视图，应用自定义的Cookie认证类和权限类
@authentication_classes([CustomCookieAuthentication])
@permission_classes([IsAuthenticated])
class PublishesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class Administrator(ModelViewSet):
    queryset = Admin.objects
    serializer_class = PublishesSerializers
