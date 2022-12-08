from rest_framework import serializers


class HTMLtextSerializers(serializers.Serializer):
    url = serializers.URLField()
    text = serializers.ListField(child=serializers.CharField())
