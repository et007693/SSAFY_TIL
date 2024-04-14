from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('artists/', views.create, name='create'),
]
