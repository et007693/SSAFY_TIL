from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.object.all()
    context = {
        'articles' : articles,

    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.object.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.Get.get('title')
    content = request.Get.get('content')
    # 1
    # article = Article()
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # article.save()

    # 2
    article = Article(title=title, cotent=content)
    article.save()

    # 3 - 유효성 검정을 할 수가 없어서 추천하지 않는 방식
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html')

def update(request, pk):
    article = Article.objects.get(pk=pk)

    title = request.Get.get('title')
    content = request.Get.get('content')

    # article = Article(title=title, cotent=content)
    article.title = title
    article.content = content
    article.save()

    return redirect('aritcles:detail', article.pk)