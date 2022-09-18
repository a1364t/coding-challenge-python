from rest_framework import serializers

class AppSerializer(serializers.Serializer):
    payload = serializers.ListField(required=True)