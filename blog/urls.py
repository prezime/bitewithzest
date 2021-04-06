from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('filter/<slug:slug>/', views.CategoryList.as_view(), name='category_view'),
    path('filter/sub/<slug:slug>/', views.SubCategoryList.as_view(), name='subcategory_view'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]