from rest_framework import status, views
from rest_framework.response import Response

from apps.artworks.serializers.artworks import ArtworkSerializer
from apps.artworks.services.artworks_service import ArtworkService


class ArtworkListCreateView(views.APIView):
    """
    GET: 전체 작품 리스트
    POST: 작품 생성
    """
    def get(self, request):
        artworks = ArtworkService.list_all()
        serializer = ArtworkSerializer(artworks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtworkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artwork = ArtworkService.create(serializer.validated_data)
        return Response(ArtworkSerializer(artwork).data, status=status.HTTP_201_CREATED)


class ArtworkDetailView(views.APIView):
    """
    GET: 상세 조회
    PUT: 수정
    DELETE: 삭제
    """
    def get_object(self, artwork_id):
        return ArtworkService.retrieve(artwork_id)

    def get(self, request, artwork_id):
        artwork = self.get_object(artwork_id)
        serializer = ArtworkSerializer(artwork)
        return Response(serializer.data)

    def put(self, request, artwork_id):
        artwork = self.get_object(artwork_id)
        serializer = ArtworkSerializer(artwork, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated = ArtworkService.update(artwork, serializer.validated_data)
        return Response(ArtworkSerializer(updated).data)

    def delete(self, request, artwork_id):
        artwork = self.get_object(artwork_id)
        ArtworkService.delete(artwork)
        return Response(status=status.HTTP_204_NO_CONTENT)
