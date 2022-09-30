from django.shortcuts import render, get_object_or_404
from .models import Post

def all_blogs(request):
    posts = Post.objects.order_by('-publish_date')
    context = {'posts': posts}
    return render(request, 'blog/all_blogs.html', context)

def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
