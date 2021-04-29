from django.shortcuts import render
from django.views import generic
from .models import User,Post,Category,SubCategory
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage





class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'index.html'
    # context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        pn = self.request.GET.get('page',1) 
        shared_context(context,pn)
        return context   

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        # pn = self.request.GET.get('page',1) 
        shared_context(context,self)
        return context
    


def shared_context(context,self):
    cat_queryset = Category.objects.all()
    context['cat_list'] = cat_queryset.filter(status=1).order_by('-id') 
    context['cat_list_asc'] = cat_queryset.filter(status=1).order_by('id') 
    subcat_queryset = SubCategory.objects.all()
    context['subcat_list'] = subcat_queryset.filter(status=1).order_by('-id') 
    context['subcat_list_asc'] = subcat_queryset.filter(status=1).order_by('id') 
    context['post_cat1'] = Category.objects.get(id=1)
    context['post_cat2'] = Category.objects.get(id=3)
    context['post_cat3'] = Category.objects.get(id=4)
    post_queryset_ascending = Post.objects.all().filter(status=1).filter(category = list(context.values())[1]).order_by('-id') 
    post_queryset_descending = Post.objects.all().filter(status=1).filter(subcategory = list(context.values())[1]).order_by('id')
    post_queryset_cat1 = Post.objects.all().filter(category = context['post_cat1'].description).filter(status=1).order_by('id')  
    post_queryset_cat2 = Post.objects.all().filter(category = context['post_cat2'].description).filter(status=1).order_by('id') 
    post_queryset_cat3 = Post.objects.all().filter(category = context['post_cat3'].description).filter(status=1).order_by('id') 
    post_queryset_featured = Post.objects.all().filter(cardtype='1').filter(status=1).order_by('id') 
    post_count = 5
    p_cat1 = Paginator(post_queryset_cat1,post_count)
    p_cat2 = Paginator(post_queryset_cat2,post_count)
    p_cat3 = Paginator(post_queryset_cat3,post_count)
    p_feat = Paginator(post_queryset_featured,post_count)
    p_asc = Paginator(post_queryset_ascending,post_count)
    p_desc = Paginator(post_queryset_descending,post_count)
    page_num = self.request.GET.get('page',1)
    try:
        post_queryset_paginated_cat1 = p_cat1.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):         
        post_queryset_paginated_cat1 = p_cat1.page(1) 
   
    try:
        post_queryset_paginated_cat2 = p_cat2.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):          
        post_queryset_paginated_cat2 = p_cat2.page(1)

    try:    
        post_queryset_paginated_cat3 = p_cat3.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):        
        post_queryset_paginated_cat3 = p_cat3.page(1)
   
    try:    
        post_queryset_paginated_feat = p_feat.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):          
        post_queryset_paginated_feat = p_feat.page(1)
   
    try:    
        post_queryset_paginated_asc = p_asc.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):         
        post_queryset_paginated_asc = p_asc.page(1)
  
    try:    
        post_queryset_paginated_desc = p_desc.page(page_num) 
    except (EmptyPage, PageNotAnInteger, InvalidPage):          
        post_queryset_paginated_desc = p_desc.page(1)  
        

    post_queryset = Post.objects.all() 

    context['post_cat_list'] = post_queryset_paginated_asc   
    context['post_subcat_list'] = post_queryset_paginated_desc
    context['post_cat1_list'] = post_queryset_paginated_cat1
    context['post_cat2_list'] = post_queryset_paginated_cat2
    context['post_cat3_list'] = post_queryset_paginated_cat3
    context['post_featured_list'] = post_queryset_paginated_feat
    context['related_posts'] = post_queryset


class CategoryList(generic.DetailView):
    model = Category
    template_name = 'post_cat_list.html'
    def get_context_data(self,**kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        shared_context(context,self)
        return context 

class SubCategoryList(generic.DetailView):
    model = SubCategory
    template_name = 'post_cat_list.html'
    def get_context_data(self, **kwargs):
        context = super(SubCategoryList, self).get_context_data(**kwargs)
        shared_context(context,self)
        return context 

class FeaturedList(ListView):
    model = Post
    template_name = 'post_cat_list.html'
    def get_context_data(self, **kwargs):
        context = super(FeaturedList, self).get_context_data(**kwargs)
        shared_context(context,self)
        return context 
        
# class RequestTest(generic.DetailView):
     

        

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
       