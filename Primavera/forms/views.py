from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def index(response):
    return render(response,'form/index.html',{})

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
        email = EmailMessage(
                'Mensaje de app Django',
                'El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}'.format(name,email,message),
                '',
                ['newhamonesjames@gmail.com'],
                reply_to=email

                
                  )
        email.send()