# models.py
```python
from django.db import models
from django.contrib.auth.models import AbstractUser(user 기본 모델)
```

# urls.py
```python
from django.urls import path
from . import views
```

# forms.py
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
        model = get_user_model()
```

# account.views.py
```python
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('index')

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# 회원삭제
def delete(request):
    auth_logout(request)
    request.user.delete()
    return redirect('accounts:login')
```

# app.views.py
```python
# user 생성(n:m)
def create_author(request):
    if request.method == 'POST':
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

# 책 생성
def books_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/books_create.html', context)

# n:m 값 return
def author_books(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    context = {
        'author':author,
        'books':books
    }
    return render(request, 'libraries/author_books.html', context)

# 구독
def author_subscribe(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    if author.subscribed_users.filter(pk=request.user.pk).exists():
        author.subscribed_users.remove(request.user)
    else:
        author.subscribed_users.add(request.user)
    return redirect('libraries:author_books', author.pk)
```

# base.html
```python
# 로그인 여부
{% if user.is_authenticated %}
```


## 그 외
```python
from django.contrib.auth import get_user_model
user = get_user_model()
```