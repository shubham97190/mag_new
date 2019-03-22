from django.shortcuts import render, HttpResponse
from article.models import Article,Category,Users
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.http import JsonResponse
import psycopg2
from django import template
register = template.Library()

# Create your views here.

class ArticleCreate(TemplateView):
    template_name='index.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = Category.objects.all()
        context['trading_post'] = Article.objects.all()[:4]
        return context

class UserCreate(CreateView ):
    template_name='registration.html'
    model=Users
    fields=['first_name','last_name','user_name','e_mail','password']
    
    
    

class ArticleViews(TemplateView):
    template_name='post.html'
    def get_context_data(self, *args,**kwargs):
        context = super(ArticleViews,self).get_context_data(*args,**kwargs)
        cat_title = Category.objects.filter(slug=kwargs['slug'])
        context['navbar'] = Category.objects.all()
        context['trading_post'] = Article.objects.all()[:4]
        context['category_article'] = Article.objects.filter(categary=cat_title[0])
        context['title']=kwargs['slug']
        return context 
