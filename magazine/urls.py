"""magazine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ArticleViews,ArticleCreate,usercreate,login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from article  import views as art_view
# from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ArticleCreate.as_view(),name='index'),
    path('registration',usercreate,name="registration"),
    path('login',login,name="login"),
    path('<slug>',ArticleViews.as_view(),name="get_article"),
    path('account_activation_sent', art_view.account_activation_sent, name='account_activation_sent'),
    path('category/category/<slug>',ArticleViews.as_view(),name="get_article"),
    path('activate/?P<uidb64>[A-Za-z_\-]+/?P<token>[A-Za-z]{1,13}-[A-Za-z]{1,20}',
        art_view.activate, name='activate'),
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
