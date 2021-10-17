from django.contrib import admin
from .models import Post, Category, SubCategory, Contibutor, Language, PostLang
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
    def id_default(self):
        RefPost = Post.objects.get(id=1)
        return (RefPost.id)
    list_display = ('title', 'slug', 'category')
    # raw_id_fields = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(SubCategory, SubCatAdmin)
admin.site.register(Contibutor)
admin.site.register(Language, LanguageAdmin)
admin.site.register(PostLang, PostLangAdmin)
