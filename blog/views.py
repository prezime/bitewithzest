from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post, PostLang, Category, SubCategory, Contibutor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.core.mail import send_mail, BadHeaderError
import urllib.request
import json
from django.conf import settings


class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'showcase.html'
    # context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        #pn = self.request.GET.get('page',1)
        shared_context(context, self)
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        # post = Post.objects.filter(slug=self.kwargs.get('slug'))
        # post.update(count=F('count') + 1)
        shared_context(context, self)
        return context


def shared_context(context, self):
    cat_queryset = Category.objects.all()
    context['cat_list'] = cat_queryset.filter(status=1).order_by('order_count')
    context['cat_list_asc'] = cat_queryset.filter(
        status=1).order_by('-order_count')
    subcat_queryset = SubCategory.objects.all()
    context['subcat_list'] = subcat_queryset.filter(
        status=1).order_by('-order_count')
    context['subcat_list_asc'] = subcat_queryset.filter(
        status=1).order_by('order_count')
    context['post_cat1'] = Category.objects.get(id=1)
    context['post_cat2'] = Category.objects.get(id=7)
    context['post_cat3'] = Category.objects.get(id=3)
    context['post_cat4'] = Category.objects.get(id=4)
    context['post_cat5'] = Category.objects.get(id=8)
    post_queryset_ascending = Post.objects.all().filter(status=1).filter(
        category=list(context.values())[1]).order_by('-custom_date', 'created_on')
    post_queryset_descending = Post.objects.all().filter(status=1).filter(
        subcategory=list(context.values())[1]).order_by('-custom_date', 'created_on')
    post_queryset_cat1 = Post.objects.all().filter(category=context['post_cat1'].description).filter(
        status=1).order_by('-custom_date', 'created_on')
    post_queryset_cat2 = Post.objects.all().filter(category=context['post_cat2'].description).filter(
        status=1).order_by('-custom_date', 'created_on')
    post_queryset_cat3 = Post.objects.all().filter(category=context['post_cat3'].description).filter(
        status=1).order_by('-custom_date', 'created_on')
    post_queryset_cat4 = Post.objects.all().filter(category=context['post_cat4'].description).filter(
        status=1).order_by('-custom_date', 'created_on')
    post_queryset_cat5 = Post.objects.all().filter(category=context['post_cat5'].description).filter(
        status=1).order_by('-custom_date', 'created_on')
    post_queryset_featured = Post.objects.all().filter(
        cardtype='1').filter(status=1).order_by('id')
    post_count = 6
    p_cat1 = Paginator(post_queryset_cat1, post_count)
    p_cat2 = Paginator(post_queryset_cat2, post_count)
    p_cat3 = Paginator(post_queryset_cat3, post_count)
    p_cat4 = Paginator(post_queryset_cat4, post_count)
    p_cat5 = Paginator(post_queryset_cat5, post_count)
    p_feat = Paginator(post_queryset_featured, post_count)
    p_asc = Paginator(post_queryset_ascending, post_count)
    p_desc = Paginator(post_queryset_descending, post_count)

    # Languages
    postlang_queryset_ascending = PostLang.objects.all().filter(status=1).filter(
        category=list(context.values())[1]).order_by('-custom_date', 'created_on')
    postlang_queryset_descending = PostLang.objects.all().filter(status=1).filter(
        subcategory=list(context.values())[1]).order_by('-custom_date', 'created_on')
    postlang_queryset_cat1 = Post.objects.all().filter(
        category=context['post_cat1'].description).filter(status=1).order_by('-custom_date', 'created_on')
    postlang_queryset_cat2 = Post.objects.all().filter(
        category=context['post_cat2'].description).filter(status=1).order_by('-custom_date', 'created_on')
    postlang_queryset_cat3 = Post.objects.all().filter(
        category=context['post_cat3'].description).filter(status=1).order_by('-custom_date', 'created_on')
    postlang_queryset_cat4 = Post.objects.all().filter(
        category=context['post_cat4'].description).filter(status=1).order_by('-custom_date', 'created_on')
    postlang_queryset_cat5 = Post.objects.all().filter(
        category=context['post_cat5'].description).filter(status=1).order_by('-custom_date', 'created_on')
    postlang_queryset_featured = PostLang.objects.all().filter(
        cardtype='1').filter(status=1).order_by('id')
    pl_cat1 = Paginator(postlang_queryset_cat1, post_count)
    pl_cat2 = Paginator(postlang_queryset_cat2, post_count)
    pl_cat3 = Paginator(postlang_queryset_cat3, post_count)
    pl_cat4 = Paginator(postlang_queryset_cat4, post_count)
    pl_cat5 = Paginator(postlang_queryset_cat5, post_count)

    pl_feat = Paginator(postlang_queryset_featured, post_count)
    pl_asc = Paginator(postlang_queryset_ascending, post_count)
    pl_desc = Paginator(postlang_queryset_descending, post_count)

    page_num = self.request.GET.get('page', 1)
    try:
        post_queryset_paginated_cat1 = p_cat1.page(page_num)
        postlang_queryset_paginated_cat1 = pl_cat1.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_cat1 = p_cat1.page(1)
        postlang_queryset_paginated_cat1 = pl_cat1.page(1)

    try:
        post_queryset_paginated_cat2 = p_cat2.page(page_num)
        postlang_queryset_paginated_cat2 = pl_cat2.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_cat2 = p_cat2.page(1)
        postlang_queryset_paginated_cat2 = pl_cat2.page(1)

    try:
        post_queryset_paginated_cat3 = p_cat3.page(page_num)
        postlang_queryset_paginated_cat3 = pl_cat3.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_cat3 = p_cat3.page(1)
        postlang_queryset_paginated_cat3 = pl_cat3.page(1)

    try:
        post_queryset_paginated_cat4 = p_cat4.page(page_num)
        postlang_queryset_paginated_cat4 = pl_cat4.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_cat4 = p_cat4.page(1)
        postlang_queryset_paginated_cat4 = pl_cat4.page(1)

    try:
        post_queryset_paginated_cat5 = p_cat5.page(page_num)
        postlang_queryset_paginated_cat5 = pl_cat5.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_cat5 = p_cat5.page(1)
        postlang_queryset_paginated_cat5 = pl_cat5.page(1)

    try:
        post_queryset_paginated_feat = p_feat.page(page_num)
        postlang_queryset_paginated_feat = pl_feat.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_feat = p_feat.page(1)
        postlang_queryset_paginated_feat = pl_feat.page(1)

    try:
        post_queryset_paginated_asc = p_asc.page(page_num)
        postlang_queryset_paginated_asc = pl_asc.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_asc = p_asc.page(1)
        postlang_queryset_paginated_asc = pl_asc.page(1)

    try:
        post_queryset_paginated_desc = p_desc.page(page_num)
        postlang_queryset_paginated_desc = pl_desc.page(page_num)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        post_queryset_paginated_desc = p_desc.page(1)
        postlang_queryset_paginated_desc = pl_desc.page(1)

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

    # Language
    postlang_queryset = PostLang.objects.all()
    context['postlang_list'] = postlang_queryset
    context['postlang_cat_list'] = postlang_queryset_paginated_asc
    context['postlang_subcat_list'] = postlang_queryset_paginated_desc
    context['postlang_cat1_list'] = postlang_queryset_paginated_cat1
    context['postlang_cat2_list'] = postlang_queryset_paginated_cat2
    context['postlang_cat3_list'] = postlang_queryset_paginated_cat3
    context['postlang_cat4_list'] = postlang_queryset_paginated_cat4
    context['postlang_cat5_list'] = postlang_queryset_paginated_cat5

    context['postlang_featured_list'] = postlang_queryset_paginated_feat


class CategoryList(generic.DetailView):
    model = Category
    template_name = 'post_cat_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        shared_context(context, self)
        return context


class SubCategoryList(generic.DetailView):
    model = SubCategory
    template_name = 'post_cat_list.html'

    def get_context_data(self, **kwargs):
        context = super(SubCategoryList, self).get_context_data(**kwargs)
        shared_context(context, self)
        return context


class FeaturedList(generic.ListView):
    model = Post
    template_name = 'post_cat_list.html'

    def get_context_data(self, **kwargs):
        context = super(FeaturedList, self).get_context_data(**kwargs)
        shared_context(context, self)
        return context


def about(request):
    cat_list = Category.objects.all().filter(status=1).order_by('order_count')
    authors_list = Contibutor.objects.all().order_by('order_count')
    return render(request, "about.html", {'cat_list': cat_list, 'authors_list': authors_list})


def cookies(request):
    cat_list = Category.objects.all().filter(status=1).order_by('order_count')
    return render(request, "cookies_info.html", {'cat_list': cat_list})


def contact(request):
    cat_list = Category.objects.all().filter(status=1).order_by('order_count')
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
            New Message: {}
            From: {}
        '''.format(contact_data['message'], contact_data['email'])

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            if subject and message and email:
                try:
                    send_mail(contact_data['subject'],
                              message, '', ['cvetje@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request, 'thankyou.html', {'cat_list': cat_list})
            else:
                # In reality we'd use a form class
                # to get proper validation errors.
                return render(request, 'invalidfields.html', {'cat_list': cat_list})
        else:
            return render(request, 'invalidfields.html', {'cat_list': cat_list})
    return render(request, "contact.html", {'cat_list': cat_list})
