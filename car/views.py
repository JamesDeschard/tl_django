from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Vehicle
from .forms import VehicleForm


def home(request):
    cars = Vehicle.objects.all()
    paginator = Paginator(cars, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    car = Vehicle.objects.get(pk=pk)
    context = {
        'car': car
    }
    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VehicleForm()

    context = {
        'title': 'Create',
        'form': form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    car = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = VehicleForm(instance=car)

    context = {
        'title': 'Update',
        'form': form
    }
    return render(request, 'create.html', context)


def delete(request, pk):
    car = Vehicle.objects.get(pk=pk)
    car.delete()
    return redirect('home')
