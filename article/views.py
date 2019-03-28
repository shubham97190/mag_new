from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from article.tokens import account_activation_token
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import auth_login

def activate(request, uidb64, token):
    try:
        print('uid64:-',uidb64)
        print('token',token)
        uid = force_text(urlsafe_base64_encode(force_bytes(uidb64)))
        # urlsafe_base64_encode(force_bytes(uidb64)).decode()
        # u=unicode(uid, "utf-8")
        print('uid',type(uid),uid,"dfgsdfshgd")
        user = User.objects.get(pk=uid)
        print('sdaguyaftgawuyfg',user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        print('shubham')

    if user is not None and account_activation_token.check_token(user, token):
        user.is_staff = True
        user.save()
        # auth_login(request, user)
        return HttpResponse('home')
    else:
        return HttpResponse('Nhi hai ')
        


def mail(*args,**kwargs):
    subject = 'Thank you for registering to our site'
    
    message = render_to_string('account_activation_email.html', {
            'user' :args[0].username ,
            'domain': kwargs['domain'],
            'uid' :  urlsafe_base64_encode(force_bytes(args[0].pk)),
            'token': account_activation_token.make_token(args),    
        })
    
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [kwargs['email'],]
    send_mail( subject, message, email_from, recipient_list )
    return True

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

