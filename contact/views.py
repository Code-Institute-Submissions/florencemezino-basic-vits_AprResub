from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


def contact_view(request):
    """Send an email to user and admin with a summary of user request """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            email_subject = render_to_string(
                    'contact/customer_emails/customer_email_subject.txt', 
                    )
            email_message = render_to_string(
                'contact/customer_emails/customer_email_body.txt', {
                    'full_name': full_name, 'email': email, 'subject': subject, 'message': message, 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                email_subject, email_message, settings.DEFAULT_FROM_EMAIL, [
                    email, settings.DEFAULT_FROM_EMAIL])
            return render(request, 'contact/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
