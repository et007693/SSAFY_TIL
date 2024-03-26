from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'todos/index.html')

def create_todo(requst):
    return render(requst, 'todos/create_todo.html')