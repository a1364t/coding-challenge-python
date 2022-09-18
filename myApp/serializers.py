from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    showImage = serializers.URLField(required=True)

class SeasonsSerializer(serializers.Serializer):
    slug = serializers.CharField(required=False)

class NextEpisodeSerializer(serializers.Serializer):
    channel = serializers.CharField(allow_null = True)
    channelLogo = serializers.URLField(required=False)
    date = serializers.DateField(allow_null = True)
    html = serializers.CharField(required=False)
    url = serializers.URLField(required=False)

class PayloadSerializer(serializers.Serializer):
    country = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    drm = serializers.BooleanField(required=False)
    episodeCount = serializers.IntegerField(required=False)
    genre = serializers.CharField(required=False)
    image = ImageSerializer(many=False, required=False)
    language = serializers.CharField(required=False)
    # seasons = SeasonsSerializer(many=False)
    primaryColour = serializers.CharField(required=False)
    nextEpisode = NextEpisodeSerializer(many=False, allow_null = True, required=False)
    slug = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    tvChannel = serializers.CharField(required=False)

class AppSerializer(serializers.Serializer):
    payload = PayloadSerializer(many=True)
    skip = serializers.IntegerField(required=False)
    take = serializers.IntegerField(required=False)
    totalRecords = serializers.IntegerField(required=False)