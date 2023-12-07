from rest_framework.viewsets import ModelViewSet
from appbook01.models import Lending
from rest_framework import serializers


class PublishesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = "__all__"


class Administrator(ModelViewSet):
    queryset = Lending.objects
    serializer_class = PublishesSerializers
