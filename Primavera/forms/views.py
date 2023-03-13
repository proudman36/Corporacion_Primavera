from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.conf import settings

def index(request):
    return render(request, 'form/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        country = request.POST['country']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['newhamonesjames@gmail.com']
        email_body = render_to_string('form/email_body.html', {'name': name, 'email': email, 'subject': subject, 'phone': phone, 'country': country, 'message': message})
        send_mail(subject, email_body, from_email, recipient_list, fail_silently=False, html_message=email_body)
        return redirect('index')
    else:
        return render(request, 'form/index.html', {})