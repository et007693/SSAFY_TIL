from django.urls import path
from . import views

app_name = 'stations'

urlpatterns = [
    path('locations/', views.location_create),
    path('stations/', views.station_list),
    path('stations/<int:station_pk>/', views.station_detail),
    path('locations/<int:location_pk>/stations/', views.station_create),
]
