from django.shortcuts import render, HttpResponse
from article.models import Article,Category
from django.views.generic.base import TemplateView
from .forms import Registration
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView
# Create your views here.


class ArticleCreate(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = Category.objects.all()
        context['trading_post'] = Article.objects.all()[:4]
        return context


class ArticleViews(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, *args,**kwargs):
        context = super(ArticleViews,self).get_context_data(*args,**kwargs)
        cat_title = Category.objects.filter(slug=kwargs['slug'])
        context['navbar'] = Category.objects.all()
        context['trading_post'] = Article.objects.all()[:4]
        context['category_article'] = Article.objects.filter(categary=cat_title[0])
        context['title']=kwargs['slug']
        return context 


def usercreate(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Sucess')
    else:
        form= Registration()
    return render(request, 'registration.html', {'form' : form})


def login(request):
    if request.method == 'POST':
        LoginView.as_view('login.html')

def email(request,**kwargs):
    subject = 'Thank you for registering to our site'
    message="it  means a world to us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]

    send_mail( subject, message, email_from, recipient_list )
    return True