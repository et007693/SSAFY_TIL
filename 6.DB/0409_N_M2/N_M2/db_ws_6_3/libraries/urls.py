from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/', views.book_list, name='book_list')
]
