from django.urls import path
from . import views

app_name = 'blog'  # This defines the namespace

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('featured/', views.featured_blog_list, name='featured_blog_list'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.category_filter, name='category_filter'),
    path('tag/<slug:slug>/', views.tag_filter, name='tag_filter'),
    path('search/', views.search, name='blog_search'),
    path('archive/<int:year>/<int:month>/', views.archive, name='blog_archive'),
    path('author/<str:username>/', views.author_articles, name='blog_author_articles'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('<slug:slug>/rate/', views.add_rating, name='add_rating'),
]
