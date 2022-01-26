from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('filter/<slug:slug>/', views.CategoryList.as_view(), name='category_view'),
    path('filter/sub/<slug:slug>/',
         views.SubCategoryList.as_view(), name='subcategory_view'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('filter/type/<cardtype>',
         views.FeaturedList.as_view(), name='featured_view'),
    path('contact/info/', views.contact, name='contact_view'),
    path('about/info/', views.about, name='about_view'),
    path('cookies/info/', views.cookies, name='cookies_view'),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),
    path("googlec6c3e7f34fb4a4d9.html", TemplateView.as_view(
        template_name="googlec6c3e7f34fb4a4d9.html", content_type="text/html"))
]
