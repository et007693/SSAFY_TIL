from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookListSerializers
from .models import Book

# Create your views here.
@api_view(['GET'])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookListSerializers(books, many=True)
        return Response(serializer.data)