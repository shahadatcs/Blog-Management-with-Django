from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from . forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been submitted, Admin will get back to you soon')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)



