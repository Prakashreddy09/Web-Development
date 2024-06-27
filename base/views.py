from django.shortcuts import render, redirect
from .models import Space
from .forms import SpaceForm

# Create your views here.

def home(request):

    spaces = Space.objects.all()
    
    context = {'spaces': spaces}

    return render(request, 'home.html', context)

def space(request, pk):

    name = Space.objects.get(id=pk)

    context = {'space': name}

    return render( request, 'space.html' ,context)


def createspace(request):

    form = SpaceForm()
    if request.method == "POST":
        form = SpaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}

    return render(request, 'room_form.html', context)


def updatespace(request):
    pass

def deletespace(request, pk):
    pass

