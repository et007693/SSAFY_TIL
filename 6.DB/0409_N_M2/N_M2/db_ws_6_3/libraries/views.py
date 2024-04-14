from django.shortcuts import render, redirect
from .forms import AuthorForm, BookFrom
from .models import Book, Author

# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('accounts:profile', author.user.username)
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/create_author.html', context)

def create_book(request):
    if request.method == "POST":
        form = BookFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:book_list')
    else:
        form = BookFrom()
    context = {
        'form':form
    }
    return render(request, 'libraries/create_book.html', context)

def book_list(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request, 'libraries/books.html', context)