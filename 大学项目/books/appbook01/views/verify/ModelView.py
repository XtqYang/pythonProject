from rest_framework.viewsets import ModelViewSet

from rest_framework import serializers

from appbook01.models import PrettyNum


class PublishesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrettyNum
        fields = "__all__"

    # 自定义验证规则
    def validate_name(self, value):
        if value.endswith("图书"):
            return value
        else:
            raise serializers.ValidationError("图书名称未以图书结尾")


class PublishView(ModelViewSet):
    queryset = PrettyNum.objects
    serializer_class = PublishesSerializers
