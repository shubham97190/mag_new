from django.contrib import admin
from article.models import Category,Article,MagazineCategory

# Register your models here.
admin.site.register(MagazineCategory)
admin.site.register(Article)
admin.site.register(Category)
