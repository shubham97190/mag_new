from django.db import models
#from users.models import Users

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='category_images/',null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    modified_date = models.DateTimeField(auto_now_add=True,null=True)
    
class MagazineCategory(models.Model):
    magazine_category = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.magazine_category 
    
class Article(models.Model):
    categary = models.ForeignKey(MagazineCategory,on_delete=models.CASCADE,null=True)
    #user_id = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,related_name="1")
    title = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=1000,null=True)
    image = models.ImageField(upload_to='article_images/',null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    modified_date = models.DateTimeField(auto_now_add=True,null=True)
    
    
    