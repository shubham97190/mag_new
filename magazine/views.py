from django.shortcuts import render, HttpResponse
from article.models import Article,Category
from django.views.generic.base import TemplateView
from .forms import Registration
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import auth_login
from django.contrib.auth import authenticate

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
        print(cat_title)
        context['navbar'] = Category.objects.all()
        context['trading_post'] = Article.objects.all()[:4]
        context['category_article'] = Article.objects.filter(categary=cat_title)
        context['title']=kwargs['slug']
       
        return context 


def usercreate(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        kwargs={}
        if form.is_valid():
            # form.save()
            email = request.POST.get('email')
            
            kwargs['email']=email
            kwargs["user"]=""
            print(kwargs['email'])
            # mail(**kwargs)
            return HttpResponse('Sucess')
    else:
        form= Registration()
    print(form.errors)
    return render(request, 'registration.html', {'form' : form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # print("They used username: {} and password: {}".format(username,password))
        # print(user)
        if user:
            if user.is_staff:
                auth_login(request,user)
                return HttpResponse(" Wellcome <b> %s</b> You are login "%(user.username) )
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

