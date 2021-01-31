from django.contrib import admin
from .models import Post,Category 
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):
#class PostAdmin(SummernoteModelAdmin):       
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",'cardtype')
    list_category = ('category')
    search_fields = ['title', 'intro', 'maintext']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('intro','maintext','preparationtext','ingredients')
  
admin.site.register(Post, PostAdmin)
admin.site.register(Category)