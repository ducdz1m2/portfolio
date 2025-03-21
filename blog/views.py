from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})