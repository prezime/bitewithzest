from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpRequest

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('filter/<slug:slug>/', views.CategoryList.as_view(), name='category_view'),
    path('filter/sub/<slug:slug>/', views.SubCategoryList.as_view(), name='subcategory_view'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('filter/type/<cardtype>', views.FeaturedList.as_view(), name='featured_view'),
    # path('get_request/', views.RequestTest.as_view(), name='request_view'),


    # path('about', views.About.as_view(), name='about'),
    # path('about/', TemplateView.as_view(template_name="about.html")),
]