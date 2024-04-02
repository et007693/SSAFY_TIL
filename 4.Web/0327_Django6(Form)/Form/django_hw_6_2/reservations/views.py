from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationFrom

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    print(reservations)
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    form = ReservationFrom()
    context = {
        'form':form
    }
    return render(request, 'reservations/new.html', context)

def create(request):
    form = ReservationFrom(request.POST)
    if form.is_valid():
        form.save()
        return redirect('reservations:index')
