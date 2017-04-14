from django.http import HttpResponse
from django.shortcuts import render, redirect
from yaba_core.forms.utils import generate_contact_form_instance
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


def about(request):
    return render(request, 'yaba/about.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'yaba/contact.html', {
            'form': generate_contact_form_instance()
        })

    # If the request method is POST
    form = generate_contact_form_instance(data=request.POST)

    if form.is_valid():
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Email the profile with the contact information
        template = get_template('yaba/email/contact_form_template.txt')
        context = Context({
            'name': name,
            'email': email,
            'message': message
        })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            settings.DEFAULT_FROM_EMAIL,
            ['fpoumian@gmail.com'],
            headers={'Reply-To': email}
        )

        email.send()
        messages.success(request, 'Your e-mail was successfully sent!')
        form = generate_contact_form_instance()

    return render(request, 'yaba/contact.html', {
        'form': form
    })
