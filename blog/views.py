from django.shortcuts import render
from django.views import generic
from .models import User,Post,Category,SubCategory
from django.views.generic import ListView



class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'index.html'
    # context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        shared_context(context)
        return context   

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    def get_context_data(self, **kwargs):
       context = super(PostDetail, self).get_context_data(**kwargs)
       shared_context(context)
       return context
 
def shared_context(context):
    cat_queryset = Category.objects.all()
    context['cat_list'] = cat_queryset.filter(status=1).order_by('-id') 
    context['cat_list_asc'] = cat_queryset.filter(status=1).order_by('id') 
    subcat_queryset = SubCategory.objects.all()
    context['subcat_list'] = subcat_queryset.filter(status=1).order_by('-id') 
    context['subcat_list_asc'] = subcat_queryset.filter(status=1).order_by('id') 
    post_queryset = Post.objects.all()
    context['post_cat_list'] = post_queryset.filter(status=1).order_by('-id') 
    context['post_subcat_list'] = post_queryset.filter(status=1).order_by('id') 
    context['related_posts'] = post_queryset
    context['post_cat1_list'] = post_queryset.filter(category='Enjoy The Food').filter(status=1).order_by('id') 
    context['post_cat1'] = Category.objects.get(id=1)
    context['post_cat2_list'] = post_queryset.filter(category='Immunity Boosting').filter(status=1).order_by('id') 
    context['post_cat2'] = Category.objects.get(id=3)
    context['post_cat3_list'] = post_queryset.filter(category='Our Planet').filter(status=1).order_by('id') 
    context['post_cat3'] = Category.objects.get(id=4)
    context['post_featured_list'] = post_queryset.filter(cardtype='1').filter(status=1).order_by('id') 


class CategoryList(generic.DetailView):
    model = Category
    template_name = 'post_cat_list.html'
    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        shared_context(context)
        return context 

class SubCategoryList(generic.DetailView):
    model = SubCategory
    template_name = 'post_cat_list.html'
    def get_context_data(self, **kwargs):
        context = super(SubCategoryList, self).get_context_data(**kwargs)
        shared_context(context)
        return context 

class FeaturedList(ListView):
    model = Post
    template_name = 'post_cat_list.html'
    def get_context_data(self, **kwargs):
        context = super(FeaturedList, self).get_context_data(**kwargs)
        shared_context(context)
        return context 
# class FeaturedList(ListView):
#     model = Post               

# class About(generic.DetailView):
#     model = User
#     template_name = 'about.html'
#     def get_context_data(self, **kwargs):
#         context = super(SubCategoryList, self).get_context_data(**kwargs)
#         shared_context(context)
#         return context   
# def About(request):
#          # return response
#     return render(request, "about.html")              
       