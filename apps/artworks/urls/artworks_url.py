from django.urls import path
from apps.artworks.views.artworks_view import (
    ArtworkListCreateView,
    ArtworkDetailView,
)

urlpatterns = [
    path("", ArtworkListCreateView.as_view(), name="artwork_list_create"),
    path("<int:artwork_id>/", ArtworkDetailView.as_view(), name="artwork_detail"),
]
