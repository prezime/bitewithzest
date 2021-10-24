from django.contrib import admin
from .models import Post, Category, SubCategory, Contributor, Language, PostLang, CategoryLang
from django.template.defaultfilters import slugify


class PostAdmin(admin.ModelAdmin):
    # class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_on', 'id')
    # list_filter = ("status",'cardtype')
    search_fields = ['title', 'intro', 'maintext']
    prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('intro','maintext','preparationtext','ingredients')


class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': (slugify('description'),)}
    list_display = ('description', 'slug', 'status', 'order_count', 'id')


class SubCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': (slugify('name'),)}


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


class PostLangAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'id')


class CategoryLangAdmin(admin.ModelAdmin):
    list_display = ('description', 'id')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(SubCategory, SubCatAdmin)
admin.site.register(Contributor)
admin.site.register(Language, LanguageAdmin)
admin.site.register(PostLang, PostLangAdmin)
admin.site.register(CategoryLang, CategoryLangAdmin)
