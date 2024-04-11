from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('books/', views.books, name='books'),
    path('books/create/', views.books_create, name='books_create'),
    path('author_books/<int:author_pk>/', views.author_books, name='author_books'),
    path('author_subscribe/<int:author_pk>/', views.author_subscribe, name='author_subscribe'),
]
