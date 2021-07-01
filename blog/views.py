from django.shortcuts import render
from django.views import generic
from .models import User,Post,Category,SubCategory,Contibutor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from .forms import ContactForm



class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'showcase.html'
    # context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        #pn = self.request.GET.get('page',1) 
        shared_context(context,self)
        return context   

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        # post = Post.objects.filter(slug=self.kwargs.get('slug'))
        # post.update(count=F('count') + 1)
        shared_context(context,self)
        return context
    


def shared_context(context,self):
    cat_queryset = Category.objects.all()
    context['cat_list'] = cat_queryset.filter(status=1).order_by('order_count') 
    context['cat_list_asc'] = cat_queryset.filter(status=1).order_by('-order_count') 
    subcat_queryset = SubCategory.objects.all()
    context['subcat_list'] = subcat_queryset.filter(status=1).order_by('-order_count') 
    context['subcat_list_asc'] = subcat_queryset.filter(status=1).order_by('order_count') 
    context['post_cat1'] = Category.objects.get(id=1)
    context['post_cat2'] = Category.objects.get(id=7)
    context['post_cat3'] = Category.objects.get(id=3)
    context['post_cat4'] = Category.objects.get(id=4)
    context['post_cat5'] = Category.objects.get(id=8)
    post_queryset_ascending = Post.objects.all().filter(status=1).filter(category = list(context.values())[1]).order_by('-id') 
    post_queryset_descending = Post.objects.all().filter(status=1).filter(subcategory = list(context.values())[1]).order_by('id')
    post_queryset_cat1 = Post.objects.all().filter(category = context['post_cat1'].description).filter(status=1).order_by('id')  
    post_queryset_cat2 = Post.objects.all().filter(category = context['post_cat2'].description).filter(status=1).order_by('id') 
    post_queryset_cat3 = Post.objects.all().filter(category = context['post_cat3'].description).filter(status=1).order_by('id') 
    post_queryset_cat4 = Post.objects.all().filter(category = context['post_cat4'].description).filter(status=1).order_by('id')  
    post_queryset_cat5 = Post.objects.all().filter(category = context['post_cat5'].description).filter(status=1).order_by('id') 
    

    post_queryset_featured = Post.objects.all().filter(cardtype='1').filter(status=1).order_by('id') 
    post_count = 5
    p_cat1 = Paginator(post_queryset_cat1,post_count)
    p_cat2 = Paginator(post_queryset_cat2,post_count)
    p_cat3 = Paginator(post_queryset_cat3,post_count)
    p_cat4 = Paginator(post_queryset_cat4,post_count)
    p_cat5 = Paginator(post_queryset_cat5,post_count)

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
        post_queryset_paginated_cat4 = p_cat4.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):        
        post_queryset_paginated_cat4 = p_cat4.page(1)

    try:    
        post_queryset_paginated_cat5 = p_cat5.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):        
        post_queryset_paginated_cat5 = p_cat5.page(1)       
   
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
    context['post_cat4_list'] = post_queryset_paginated_cat4
    context['post_cat5_list'] = post_queryset_paginated_cat5

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

class FeaturedList(generic.ListView):
    model = Post
    template_name = 'post_cat_list.html'
    def get_context_data(self, **kwargs):
        context = super(FeaturedList, self).get_context_data(**kwargs)
        shared_context(context,self)
        return context 
               

class About(generic.TemplateView):
    template_name = 'about.html'
    # def get_context_data(self, **kwargs):
    #     context = super(About, self).get_context_data(**kwargs)
    #     shared_context(context,self)
    #     return context  
class Contact(generic.TemplateView):
    template_name = 'contact.html'         
# class Contact(generic.FormView):
#     template_name = 'contact.html'
#     from_class = ContactForm 
#     success_url = '/contact/'
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)
# 
# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 		    body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# 			}
# 			message = "\n".join(body.values())

# 			try:
# 				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 			return redirect ("main:homepage")
      
# 	form = ContactForm()
# 	return render(request, "main/contact.html", {'form':form})            
       