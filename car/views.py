from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Vehicle
from .forms import VehicleForm, CommentForm


def search(request):
    search = request.GET.get('search')
    cars = Vehicle.objects.filter(car_name__icontains=search)
    return render(request, 'search.html', {'cars': cars, 'search': search})


def home(request):
    cars = Vehicle.objects.all()

    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
 
    context = {'cars': cars}
    return render(request, 'home.html', context)


def detail(request, pk):
    car = Vehicle.objects.get(pk=pk)
    comments = car.comment_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.vehicle = car
            comment.save()
            return redirect('detail', pk=pk)
    
    else:
        form = CommentForm()

    context = {'car': car, 'comments': comments, 'form': form}
    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VehicleForm()

    context = {'title': 'Create', 'form': form}
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

    context = {'title': 'Update', 'id': pk, 'form': form}
    return render(request, 'create.html', context)


def delete(request, pk):
    car = Vehicle.objects.get(pk=pk)
    car.delete()
    return redirect('home')
