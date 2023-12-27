from django import forms
from .models import ContactForm


class ContactFormFields(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'title', 'email', 'text')
        error_messages = None
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'text': forms.Textarea(attrs={"class": "form-control"})
        }
