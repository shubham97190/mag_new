from django.contrib import admin
from article.models import Category,Article,Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)


class show_article(admin.ModelAdmin):
    list_display=('categary','title','description','created_date')
admin.site.register(Article,show_article)