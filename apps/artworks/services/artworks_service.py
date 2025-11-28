from django.shortcuts import get_object_or_404
from apps.artworks.models import Artwork

class ArtworkService:

    @staticmethod
    def list_all():
        return Artwork.objects.all()

    @staticmethod
    def retrieve(artwork_id: int):
        return get_object_or_404(Artwork, id=artwork_id)

    @staticmethod
    def create(validated_data):
        return Artwork.objects.create(**validated_data)

    @staticmethod
    def update(artwork: Artwork, validated_data):
        for key, value in validated_data.items():
            setattr(artwork, key, value)
        artwork.save()
        return artwork

    @staticmethod
    def delete(artwork: Artwork):
        artwork.delete()
        return True
