from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    def get_context_data(self, **kwargs):
       context = super(PostDetail, self).get_context_data(**kwargs)
       context['side_post_list'] = Post.objects.filter(status=1).order_by('-created_on').exclude(id=self.get_object().id)
       return context
 



