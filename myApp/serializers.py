from rest_framework import serializers

class AppSerializer(serializers.Serializer):
    payload = serializers.ListField(child = serializers.DictField(required=True))
    # skip = serializers.IntegerField()
    # take = serializers.IntegerField()
    # totalRecords = serializers.IntegerField()