from django.urls import path
from . import views


app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:store_pk>/product', views.product, name='product'),
]
