from django.shortcuts import render
from django.views import generic
from .models import Post,Category,SubCategory



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

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


