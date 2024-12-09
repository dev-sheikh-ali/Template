# src/blog/admin.py
from django.contrib import admin
from .models import BlogPost, Category, Tag, Comment, Rating

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'featured', 'created_at', 'cover_image')
    list_filter = ('status', 'author', 'category', 'tags', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog_post', 'created_at')
    list_filter = ('blog_post', 'created_at')
    search_fields = ('content',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog_post', 'score')
    list_filter = ('score', 'blog_post')
