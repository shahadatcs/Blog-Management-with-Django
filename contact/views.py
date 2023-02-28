from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    user_id = request.POST['user_id']

    #  Check if user has made message already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already send message')
    contact = Contact(name=name, email=email, subject=subject, message=message)
    contact.save()

    # Send email
    # send_mail(
    #   'Blog message send',
    #   'There has been an message for ',
    #   'admin@gmail.com',
    #   [user_email, 'shahadat@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your message has been submitted, Admin will get back to you soon')
  else:
     return render(request, 'contact/contact.html')

