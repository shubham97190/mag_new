from django.shortcuts import render, HttpResponse
from article.models import Article,Category
from django.views.generic.edit import CreateView
import psycopg2

# Create your views here.
def index(request):
    article_qurey_set=""
    category_qurey_set=""
    try:
        category_qurey_set = Category.objects.all()
        article_qurey_set = Article.objects.all()[:4]
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    context = {'navbar':category_qurey_set,
                'trading_post':article_qurey_set     
    
    }
    return render(request,'index.html',context)

def get_article(request,slug):
    article_qurey_set=""
    category_qurey_set=""
    try:
        category_qurey_set = Category.objects.all()
        cat_title = Category.objects.filter(slug=slug)
        article_qurey_set = Article.objects.filter(categary=cat_title[0])
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    context = {'navbar':category_qurey_set,
                'trading_post':article_qurey_set,
                'title':slug,    
    
    }
    return render(request,'post.html',context)


class ArticleCreate(CreateView):
    model=Article
    fields=['first_name','last_name','user_name','e_mail','password']