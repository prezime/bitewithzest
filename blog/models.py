from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import os, shutil
from django.urls import reverse
from django.conf import settings



def path_and_rename(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/thumbs'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_thumb'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    fullname = os.path.join(settings.MEDIA_ROOT, upload_to)    
    if os.path.exists(fullname):
        shutil.rmtree(fullname)     
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_intro(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/intro'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_intro'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    fullname = os.path.join(settings.MEDIA_ROOT, upload_to)    
    if os.path.exists(fullname):
        shutil.rmtree(fullname)     
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_main(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/main'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_main'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    fullname = os.path.join(settings.MEDIA_ROOT, upload_to)    
    if os.path.exists(fullname):
        shutil.rmtree(fullname) 
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_add(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/add'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_add'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    fullname = os.path.join(settings.MEDIA_ROOT, upload_to)    
    if os.path.exists(fullname):
        shutil.rmtree(fullname)     
    # return the whole path to the file
    return os.path.join(upload_to, filename)


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Un-Publish")
)

CARDTYPE = (
    (0,"Big"),
    (1,"Small")
)


class Category(models.Model):
    description = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200,unique=True, default='')

    class Meta:
        verbose_name_plural = 'Categories'   
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')   

cats = Category.objects.all().values_list('description','description')
category_list = []
for item in cats:
  category_list.append(item) 

 
class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=200, choices=category_list, default='')
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200,unique=True, default='')
    class Meta:
        verbose_name_plural = 'Sub Categories'   
    def __str__(self):
            return self.name
  

subcats = SubCategory.objects.all().values_list('name','name')
subcategory_list = []
for item in subcats:
    subcategory_list.append(item)           

class Post(models.Model):
    titleplus = models.CharField(max_length=200, default='')
    
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, choices=category_list, default='')
    subcategory = models.CharField(max_length=200, choices=subcategory_list, default='uncategorized')
    status = models.IntegerField(choices=STATUS, default=0)
    cardtype = models.IntegerField(choices=CARDTYPE, default=0)

    thumbnail = models.FileField(upload_to=path_and_rename,blank=True)
    thumbnail_desc = models.CharField(max_length=200,default='',blank=True)
    intro_pic= models.FileField(upload_to=path_and_rename_intro,blank=True)
    intro_pic_desc = models.CharField(max_length=200,default='',blank=True)
    intro = models.TextField()
    title = models.CharField(max_length=200, unique=True)
    maintext = models.TextField(default='')
    intro1 = models.TextField(default='',blank=True)
    legend = models.TextField(default='',blank=True)
    add_pic = models.FileField(upload_to=path_and_rename_add,blank=True)
    add_pic_desc = models.CharField(max_length=200,default='',blank=True)
    ingredients = models.TextField(blank=True)
    preparationtext = models.TextField(default='',blank=True)
    main_pic = models.FileField(upload_to=path_and_rename_main,blank=True)
    main_pic_desc = models.CharField(max_length=200,default='',blank=True)
    tip = models.TextField(default='',blank=True)
    relates_to = models.ForeignKey('self', on_delete=models.CASCADE, default=1)
    relates_to_desc = models.CharField(max_length=300,default='',blank=True)
    outro = models.TextField(default='',blank=True)
    
    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('home')


