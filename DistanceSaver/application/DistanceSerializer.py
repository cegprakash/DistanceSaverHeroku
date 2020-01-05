from rest_framework import serializers


class DistanceSerializer(serializers.Serializer):
    distance = serializers.IntegerField(required=True, min_value=0, max_value=5000)