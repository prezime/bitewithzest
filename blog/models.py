from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import os
from django.urls import reverse


def path_and_rename(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/thumbs'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_thumb'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
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
    # return the whole path to the file
    return os.path.join(upload_to, filename)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

CARDTYPE = (
    (0,"Big"),
    (1,"Small")
)

class Category(models.Model):
    description = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')   

cats = Category.objects.all().values_list('description','description')
category_list = []
for item in cats:
  category_list.append(item) 

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    titleplus = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default='')
    status = models.IntegerField(choices=STATUS, default=0)
    cardtype = models.IntegerField(choices=CARDTYPE, default=0)


    intro = models.TextField()
    intro1 = models.TextField(default='',blank=True)
    maintext = models.TextField(default='')

    preparationtext = models.TextField(default='',blank=True)
    ingredients = models.TextField(default='',blank=True)

    tip = models.TextField(default='',blank=True)
    
    thumbnail = models.FileField(upload_to=path_and_rename,blank=True)
    intro_pic= models.FileField(upload_to=path_and_rename_intro,blank=True)
    main_pic = models.FileField(upload_to=path_and_rename_main,blank=True)
    add_pic = models.FileField(upload_to=path_and_rename_add,blank=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')    
