from rest_framework import serializers

class imageSerializer(serializers.Serializer):
    showImage = serializers.URLField(required=True)

class PayloadSerializer(serializers.Serializer):
    country = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    drm = serializers.BooleanField(required=False)
    episodeCount = serializers.IntegerField(required=False)
    genre = serializers.CharField(required=False)
    image = imageSerializer(many=False)
    language = serializers.CharField(required=False)

    primaryColour = serializers.CharField(required=False)

    slug = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    tvChannel = serializers.CharField(required=False)

class AppSerializer(serializers.Serializer):
    payload = PayloadSerializer(many=True)
    skip = serializers.IntegerField(required=False)
    take = serializers.IntegerField(required=False)
    totalRecords = serializers.IntegerField(required=False)