from django.shortcuts import render, HttpResponse
import psycopg2
from article.models import Article,MagazineCategory

# Create your views here.
def index(request):
    article_qurey_set=""
    magazine_category_qurey_set=""
    try:
        magazine_category_qurey_set = MagazineCategory.objects.all()
        article_qurey_set = Article.objects.all()[:4]
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    context = {'navbar':magazine_category_qurey_set,
                'trading_post':article_qurey_set     
    
    }
    return render(request,'index.html',context)

