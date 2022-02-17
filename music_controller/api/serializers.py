from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # every model has "ID" field
        field = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')