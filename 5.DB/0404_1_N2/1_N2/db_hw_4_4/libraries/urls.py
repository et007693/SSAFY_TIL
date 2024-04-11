from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:book_pk>/review', views.create_review, name='review'),
    path('<int:book_pk>/review/<int:review_pk>/delete', views.delete_comment, name='delete')
]
