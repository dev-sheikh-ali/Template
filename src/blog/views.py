from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import BlogPost, Category, Tag, Comment, Rating
from django.contrib import messages 

# Blog List View
def blog_list(request):
    posts = BlogPost.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 10)  # 10 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/blog_article_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
    })



# Featured Blogs View
def featured_blog_list(request):
    featured_posts = BlogPost.objects.filter(featured=True, status='published').order_by('-created_at')[:5]
    return render(request, 'blog/featured_blog_list.html', {
        'featured_posts': featured_posts,
    })


# Blog Detail View
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.views += 1  # Increment view count
    post.save()

    related_posts = BlogPost.objects.filter(category=post.category, status='published').exclude(id=post.id)[:5]
    comments = Comment.objects.filter(blog_post=post).order_by('created_at')

    # Pass the range for stars to the template
    stars_range = range(1, 6)

    return render(request, 'blog/blog_article_detail.html', {
        'post': post,
        'related_posts': related_posts,
        'comments': comments,
        'stars_range': stars_range,
    })



# Category Filter View
def category_filter(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_article_list.html', {
        'page_obj': page_obj,
        'category': category,
    })


# Tag Filter View
def tag_filter(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_article_list.html', {
        'page_obj': page_obj,
        'tag': tag,
    })


# Search View
def search(request):
    query = request.GET.get('q', '')
    posts = BlogPost.objects.filter(status='published', title__icontains=query) if query else []
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_search_results.html', {
        'page_obj': page_obj,
        'query': query,
    })


# Archive View
def archive(request, year, month):
    posts = BlogPost.objects.filter(status='published', created_at__year=year, created_at__month=month).order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_archives.html', {
        'page_obj': page_obj,
        'year': year,
        'month': month,
    })


# Add Comment View (Requires Authentication)
@login_required
def add_comment(request, slug):
    if request.method == "POST":
        blog_post = get_object_or_404(BlogPost, slug=slug)
        content = request.POST.get('content', '').strip()
        if content:
            Comment.objects.create(user=request.user, blog_post=blog_post, content=content)
        return redirect(blog_post.get_absolute_url())
    return JsonResponse({'error': 'Invalid request'}, status=400)


# Add Rating View (Requires Authentication)
@login_required
def add_rating(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST":
        try:
            score = int(request.POST.get('score', 0))
            if 1 <= score <= 5:  # Ensure the score is within a valid range
                rating, created = Rating.objects.update_or_create(
                    user=request.user,
                    blog_post=blog_post,
                    defaults={'score': score},
                )
                # Add a success message
                messages.success(request, f"Your rating of {rating.score} has been submitted!")
            else:
                messages.error(request, "Invalid score. Please select a score between 1 and 5.")
        except ValueError:
            messages.error(request, "Invalid score. Please try again.")
        
        # Redirect back to the blog post detail page
        return redirect(blog_post.get_absolute_url())

    # Redirect to blog detail page for GET requests
    return redirect(blog_post.get_absolute_url())

# Author Articles View
def author_articles(request, username):
    posts = BlogPost.objects.filter(author__username=username, status='published').order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_author_articles.html', {
        'page_obj': page_obj,
        'author': username,
    })
