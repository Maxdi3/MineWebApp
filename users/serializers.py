from rest_framework import serializers
from datetime import datetime

from users.models import Users


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    machine_name = serializers.CharField()
    location_long = serializers.CharField()
    location_lat = serializers.CharField()
    status = serializers.IntegerField()
    icon = serializers.IntegerField()

    def create(self,validated_data):
        validated_data['last_update'] = datetime.now()
        instance=Users.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.last_update = datetime.now()
        instance.location_long = validated_data.get('location_long')
        instance.location_lat = validated_data.get('location_lat')
        instance.status = validated_data.get('status')
        instance.icon = validated_data.get('icon')
        instance.save()
        return instance
