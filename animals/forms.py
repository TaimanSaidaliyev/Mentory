from django import forms
from animals.models import Breeds, AnimalClass


class AddBreedForm(forms.ModelForm):
    class Meta:
        model = Breeds
        fields = ('title', 'animal_type', 'description', 'photo')
        error_messages = None
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'animal_type': forms.Select(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
        }


class AddAnimalForm(forms.ModelForm):
    class Meta:
        model = AnimalClass
        fields = ('title', 'photo')
        error_messages = None
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class":"form-control"}),
        }
