from django.shortcuts import render, redirect
from animals.models import *
from .forms import AddBreedForm, AddAnimalForm
from django.urls import reverse


def view_animals_list(request):
    template = 'animals/animals_mainpage.html'
    animals_list = AnimalClass.objects.all()
    breeds_list = Breeds.objects.all()
    context = {
        'animals_list': animals_list,
        'breeds_list': breeds_list,
    }
    return render(request, template, context)


def add_animal_breed(request):
    template = 'animals/breed_add.html'
    form = AddBreedForm(request.POST, request.FILES)
    model = Breeds

    if request.method == 'POST':
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            return redirect(reverse('animal_main'))
    context = {
        'form': form
    }
    return render(request, template, context)


def add_animal_type(request):
    template = 'animals/animals_add.html'
    form = AddAnimalForm(request.POST, request.FILES)
    model = AnimalClass

    if request.method == 'POST':
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            return redirect(reverse('animal_main'))
    context = {
        'form': form
    }
    return render(request, template, context)


def animal_detail(request, breed_id):
    template = 'animals/animal_detail.html'
    animal = Breeds.objects.get(pk=breed_id)
    context = {
        'animal': animal
    }
    return render(request, template, context)