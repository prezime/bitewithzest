from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import os
import shutil
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from blog import path_rename


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Un-Publish")
)

CARDTYPE = (
    (0, "Normal"),
    (1, "Featured")
)


class Language(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=20)
    inactive = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


llist = Language.objects.filter(inactive=False)
list1 = []
for rs in llist:
    list1.append((rs.code, rs.name))
langlist = (list1)


class Contibutor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    inactive = models.BooleanField(default=False)
    description = RichTextUploadingField(default='', blank=True)
    pic = models.FileField(
        upload_to=path_rename.path_and_rename_author, blank=True)
    order_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


contributors = Contibutor.objects.all().values_list('name', 'name')
contributor_list = []
for item in contributors:
    contributor_list.append(item)


class Category(models.Model):
    description = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True, default='')
    order_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')


cats = Category.objects.all().values_list('description', 'description')
category_list = []
for item in cats:
    category_list.append(item)


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=200, choices=category_list, default='')
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True, default='')
    order_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name


subcats = SubCategory.objects.all().values_list('name', 'name')
subcategory_list = []
for item in subcats:
    subcategory_list.append(item)


class Post(models.Model):
    titleplus = models.TextField(max_length=240, default='')

    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    author = models.CharField(
        max_length=200, choices=contributor_list, default='')

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    custom_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(
        max_length=200, choices=category_list, default='')
    subcategory = models.CharField(
        max_length=200, choices=subcategory_list, default='uncategorized')
    status = models.IntegerField(choices=STATUS, default=0)
    cardtype = models.IntegerField(choices=CARDTYPE, default=0)

    thumbnail = models.FileField(
        upload_to=path_rename.path_and_rename, blank=True)
    thumbnail_desc = models.CharField(max_length=200, default='', blank=True)
    opener_pic = models.FileField(
        upload_to=path_rename.path_and_rename_opener, blank=True)

    intro = RichTextUploadingField()
    title = models.CharField(max_length=200, unique=True)
    title_invisible = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    maintext = RichTextUploadingField(default='')
    intro1 = RichTextUploadingField(default='', blank=True)
    intro_pic = models.FileField(
        upload_to=path_rename.path_and_rename_intro, blank=True)
    intro_pic_desc = models.CharField(max_length=200, default='', blank=True)
    legend = RichTextUploadingField(default='', blank=True)
    add_pic = models.FileField(
        upload_to=path_rename.path_and_rename_add, blank=True)
    add_pic_desc = models.CharField(max_length=200, default='', blank=True)
    ingredients = RichTextField(blank=True)
    preparationtext = RichTextUploadingField(default='', blank=True)
    additionaltext = RichTextUploadingField(default='', blank=True)
    main_pic = models.FileField(
        upload_to=path_rename.path_and_rename_main, blank=True)
    main_pic_desc = models.CharField(max_length=200, default='', blank=True)
    tip = RichTextField(default='', blank=True)
    relates_to = models.ForeignKey('self', on_delete=models.CASCADE, default=1)
    relates_to_desc = models.CharField(max_length=300, default='', blank=True)
    outro = RichTextUploadingField(default='', blank=True)
    credits = RichTextUploadingField(default='', blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('home')


class PostLang(models.Model):
    def save(self):
        if not self.id:
            self.id = self.post.id
        if not self.updated_on:
            self.updated_on = self.post.updated_on
        if not self.created_on:
            self.created_on = self.post.created_on
        if not self.custom_date:
            self.custom_date = self.post.custom_date
        if not self.status:
            self.status = self.post.status
        if not self.cardtype:
            self.cardtype = self.post.cardtype
        if not self.titleplus:
            self.titleplus = self.post.titleplus
        if not self.maintext:
            self.maintext = self.post.maintext
        if not self.intro1:
            self.intro1 = self.post.intro1
        if not self.intro:
            self.intro = self.post.intro
        if not self.legend:
            self.legend = self.post.legend
        if not self.ingredients:
            self.ingredients = self.post.ingredients
        if not self.additionaltext:
            self.additionaltext = self.post.additionaltext
        if not self.preparationtext:
            self.preparationtext = self.post.preparationtext
        if not self.tip:
            self.tip = self.post.tip
        if not self.outro:
            self.outro = self.post.outro
            super(PostLang, self).save()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #id = models.IntegerField(primary_key=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    custom_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cardtype = models.IntegerField(choices=CARDTYPE, default=0)
    lang = models.CharField(max_length=5, choices=langlist)
    titleplus = models.TextField(max_length=240, default='', blank=True)
    category = models.CharField(
        max_length=200, choices=category_list, default='')
    subcategory = models.CharField(
        max_length=200, choices=subcategory_list, default='uncategorized')
    intro = RichTextUploadingField(blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    maintext = RichTextUploadingField(default='', blank=True)
    intro1 = RichTextUploadingField(default='', blank=True)
    legend = RichTextUploadingField(default='', blank=True)
    ingredients = RichTextField(blank=True)
    preparationtext = RichTextUploadingField(default='', blank=True)
    additionaltext = RichTextUploadingField(default='', blank=True)
    tip = RichTextField(default='', blank=True)
    outro = RichTextUploadingField(default='', blank=True)
    credits = RichTextUploadingField(default='', blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = 'Post Languages'
