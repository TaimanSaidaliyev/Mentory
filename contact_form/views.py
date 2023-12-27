from django.shortcuts import render, redirect
from .forms import ContactFormFields
from .models import ContactForm
from django.urls import reverse


def add_contact_form(request):
    template = 'contact_form/add_form.html'
    form = ContactFormFields(request.POST, request.FILES)
    model = ContactForm

    if request.method == 'POST':
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            return redirect(reverse('contact_form_success'))
        else:
            return redirect(reverse('contact_form_not_success'))
    context = {
        'form': form
    }
    return render(request, template, context)


def success_page(request):
    template = 'contact_form/success_form.html'
    return render(request, template)


def not_success_page(request):
    template = 'contact_form/not_success_form.html'
    return render(request, template)