from django.shortcuts import render, HttpResponse
from article.models import Article,Category,Users
from django.views.generic.edit import CreateView
import psycopg2

# Create your views here.

def get_article(request,slug):
    article_qurey_set=""
    category_qurey_set=""
    category_article=""
    try:
        category_qurey_set = Category.objects.all()
        cat_title = Category.objects.filter(slug=slug)
        category_article = Article.objects.filter(categary=cat_title[0])
        article_qurey_set = Article.objects.all()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    context = {'navbar':category_qurey_set,
                'trading_post':article_qurey_set,
                'title':slug,
                'category_article' :category_article,   
    
    }
    return render(request,'post.html',context)


class ArticleCreate(CreateView):
    template_name='index.html'
    model=Users
    fields=['first_name','last_name','user_name','e_mail','password']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = Category.objects.all()
        context['trading_post'] = Article.objects.all()[:4]
        return context

class ArticleViews(CreateView):
    template_name='post.html'
    model=Users
    fields=['first_name','last_name','user_name','e_mail','password']
    def get_context_data(self, **kwargs):
        context = super(ArticleCreate,self).get_context_data(**kwargs)
        cat_title = Category.objects.filter(slug=slug)
        context['category_article'] = Article.objects.filter(categary=cat_title[0])

        return context 
