from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


from .models import Artist
from .serializers import ArtistSerialzer

# Create your views here.
@api_view(['POST'])
def create(request):
    if request.method == "POST":
        serializer = ArtistSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)