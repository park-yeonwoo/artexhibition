from rest_framework import serializers
from apps.artworks.models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = [
            "id",
            "title",
            "img_url",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
