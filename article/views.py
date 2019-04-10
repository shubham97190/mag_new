from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from article.tokens import account_activation_token
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=int(uid))
       
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
     
    if user is not None and account_activation_token.check_token(user, token):
        user.is_staff = True
        user.save()
        # auth_login(request, user)
        return HttpResponse('home')
    else:
        return HttpResponse('Nhi hai ')
        
def mail(*args,**kwargs):
    user = User.objects.get(pk=int(args[0].pk))
    subject = 'Thank you for registering to our site'

    
    message =render_to_string('account_activation_email.html', {
            'user' :user,
            'domain': kwargs['domain'],
            'uid' :  urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),    
        })
    
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [kwargs['email'],]
    send_email = EmailMultiAlternatives( subject, message, email_from, recipient_list )
    send_email.attach_alternative(message, "text/html")
    send_email.send()
    return True

def account_activation_sent(request):
    
    return render(request, 'account_activation_sent.html')

