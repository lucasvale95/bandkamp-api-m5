from rest_framework import serializers
from albums.serializers import AlbumSerializer
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album_id']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)