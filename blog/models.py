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
import deepl
from django.core.exceptions import ValidationError
translator = deepl.Translator("bfec5fb4-82b8-d470-2bb6-1eff0c6b7e84:fx")


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


class Contributor(models.Model):
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


contributors = Contributor.objects.all().values_list('name', 'name')
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


class CategoryLang(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, unique=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    lang = models.CharField(max_length=5, choices=langlist, default=0)
    slug = models.SlugField(max_length=200, editable=True, blank=True)
    order_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Category Languages'

    def __str__(self):
        return self.category.slug

    def save(self):
        if not self.id:
            if catLangExists(self.category):
                raise ValidationError('Category Language already exists')
            self.id = self.category.id
        if self.category.slug:
            self.slug = self.category.slug
        if not self.description:
            if self.category.description:
                self.description = translator.translate_text(
                    self.category.description, target_lang=self.lang)
        if self.category.order_count:
            self.order_count = self.category.order_count

        super(CategoryLang, self).save()


catlangs = CategoryLang.objects.all().values_list('description', 'description')
categorylang_list = []
for item in catlangs:
    categorylang_list.append(item)


def catLangExists(CatLang):
    if CategoryLang.objects.filter(id=CatLang.id):
        return True
    else:
        return False


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
    thumbnail_desc = models.CharField(
        max_length=200, default='', blank=True)
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
    intro_pic_desc = models.CharField(
        max_length=200, default='', blank=True)
    legend = RichTextUploadingField(default='', blank=True)
    add_pic = models.FileField(
        upload_to=path_rename.path_and_rename_add, blank=True)
    add_pic_desc = models.CharField(max_length=200, default='', blank=True)
    ingredients = RichTextField(blank=True)
    preparationtext = RichTextUploadingField(default='', blank=True)
    additionaltext = RichTextUploadingField(default='', blank=True)
    main_pic = models.FileField(
        upload_to=path_rename.path_and_rename_main, blank=True)
    main_pic_desc = models.CharField(
        max_length=200, default='', blank=True)
    tip = RichTextField(default='', blank=True)
    relates_to = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=1)
    relates_to_desc = models.CharField(
        max_length=300, default='', blank=True)
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # id = models.IntegerField(primary_key=True)
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
    title = models.CharField(max_length=200, unique=True, blank=True)
    slug = models.SlugField(max_length=200, editable=False)
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
        return self.post.slug

    def save(self):
        if not self.id:
            if postLangExists(self.post):
                raise ValidationError('Post Language already exists')
            self.id = self.post.id
        if not self.updated_on:
            self.updated_on = self.post.updated_on
        if not self.created_on:
            self.created_on = self.post.created_on
        if not self.custom_date:
            self.custom_date = self.post.custom_date
        if not self.cardtype:
            self.cardtype = self.post.cardtype
        self.category = self.post.category
        if not self.title:
            if self.post.title:
                self.title = translator.translate_text(
                    self.post.title, target_lang=self.lang)
        if not self.titleplus:
            if self.post.titleplus:
                self.titleplus = translator.translate_text(
                    self.post.titleplus, target_lang=self.lang)
        if not self.maintext:
            if self.post.maintext:
                self.maintext = translator.translate_text(
                    self.post.maintext, target_lang=self.lang)
        if not self.intro1:
            if self.post.intro1:
                self.intro1 = translator.translate_text(
                    self.post.intro1, target_lang=self.lang)
        if not self.intro:
            if self.post.intro:
                self.intro = translator.translate_text(
                    self.post.intro, target_lang=self.lang)
        if not self.legend:
            if self.post.legend:
                self.legend = translator.translate_text(
                    self.post.legend, target_lang=self.lang)
        if not self.ingredients:
            if self.post.ingredients:
                self.ingredients = translator.translate_text(
                    self.post.ingredients, target_lang=self.lang)
        if not self.additionaltext:
            if self.post.additionaltext:
                self.additionaltext = translator.translate_text(
                    self.post.additionaltext, target_lang=self.lang)
        if not self.preparationtext:
            if self.post.preparationtext:
                self.preparationtext = translator.translate_text(
                    self.post.preparationtext, target_lang=self.lang)
        if not self.tip:
            if self.post.tip:
                self.tip = translator.translate_text(
                    self.post.tip, target_lang=self.lang)
        if not self.outro:
            if self.post.outro:
                self.outro = translator.translate_text(
                    self.post.outro, target_lang=self.lang)
        if self.post.slug:
            self.slug = self.post.slug
        super(PostLang, self).save()

    class Meta:
        verbose_name_plural = 'Post Languages'


def postLangExists(PostLangParameter):
    if PostLang.objects.filter(id=PostLangParameter.id):

        return True
    else:
        return False
