from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistsSerializer


# Create your views here.
@api_view(['GET','POST'])
def artist_list_or_create(request):
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == "GET":
        artists = Artist.objects.all()
        serializer = ArtistsSerializer(artists, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == "GET":
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)