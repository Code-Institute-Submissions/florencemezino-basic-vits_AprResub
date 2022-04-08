from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email') 
            subject = form.cleaned_data.get('subject') 
            message = form.cleaned_data.get('message') 
            send_mail(subject, message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, 'contact/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def _send_confirmation_email(self, request):
    """Send the user a confirmation email"""
    cust_email = request.email
    subject = render_to_string(
        'contact/confirmation_emails/confirmation_email_subject.txt',
        )
    body = render_to_string(
        'contact/confirmation_emails/confirmation_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})
    
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
        )   