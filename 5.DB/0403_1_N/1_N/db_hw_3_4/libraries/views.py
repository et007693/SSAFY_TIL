from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import CreateForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    form = CreateForm()
    context = {
        'author': author,
        'books' : books,
        'form' : form
    }
    return render(request, 'libraries/detail.html', context)

def create(request, author_pk):
    if request.method == 'POST':
        author = Author.objects.get(pk= author_pk)
        form = CreateForm(request.POST)  # form의 입력값을 받아옴
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect('libraries:detail', author_pk)
    context = {
        'form' : form,
        'author' : author,
        'book' : book,
    }
    return render(request, 'articles/detail.html', context)

    
