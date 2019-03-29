from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30,null=True)
    slug = models.SlugField(max_length=250,null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    modified_date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title
   
class Tag(models.Model):
    word = models.CharField(max_length=35)
    slug = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.word
    
#
class Article(models.Model):
    categary = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=1000,null=True)
    image = models.ImageField(upload_to='article_images/',null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    modified_date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag,related_name='Category')
    
    def __str__(self):
        return  self.title 
    
    