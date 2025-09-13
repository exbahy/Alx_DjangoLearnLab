from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@permission_required('blog.can_view_post', raise_exception=True)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@permission_required('blog.can_create_post', raise_exception=True)
def post_create(request):
    return render(request, 'blog/post_form.html')

@permission_required('blog.can_edit_post', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_form.html', {'post': post})
