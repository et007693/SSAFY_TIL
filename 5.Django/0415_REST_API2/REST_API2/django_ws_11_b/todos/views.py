from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer

# Create your views here.
@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['DELETE'])
def todo_detail(request, todo_pk):
    if request.method == "DELETE":
        Todo.objects.get(pk=todo_pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)