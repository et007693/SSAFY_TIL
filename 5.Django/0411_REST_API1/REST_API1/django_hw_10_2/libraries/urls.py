from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('libraries/', views.book_list),
]