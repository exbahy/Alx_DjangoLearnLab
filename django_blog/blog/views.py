from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

# Register view
def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)  # auto login after registration
			return redirect('profile')
	else:
		form = RegisterForm()
	return render(request, 'blog/register.html', {'form': form})


# Login view
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('profile')
	else:
		form = AuthenticationForm()
	return render(request, 'blog/login.html', {'form': form})


# Logout view
def logout_view(request):
	logout(request)
	return redirect('login')


# Profile view
@login_required
def profile_view(request):
	return render(request, 'blog/profile.html', {'user': request.user})


class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		from .forms import CommentForm
		context['comment_form'] = CommentForm()
		context['comments'] = self.object.comments.all()
		return context


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/post_form.html'
	success_url = reverse_lazy('post-list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		response = super().form_valid(form)
		# tags handled by ModelForm
		return response


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/post_form.html'
	success_url = reverse_lazy('post-list')

	def test_func(self):
		post = self.get_object()
		return post.author == self.request.user


def posts_by_tag(request, tag_name):
	posts = Post.objects.filter(tags__name__iexact=tag_name).distinct()
	return render(request, 'blog/tag_posts.html', {'posts': posts, 'tag_name': tag_name})


def search_posts(request):
	query = request.GET.get('q', '')
	results = []
	if query:
		results = Post.objects.filter(
			Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
		).distinct()
	return render(request, 'blog/search_results.html', {'results': results, 'query': query})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_url = reverse_lazy('post-list')

	def test_func(self):
		post = self.get_object()
		return post.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm

	def form_valid(self, form):
		post_pk = self.kwargs.get('pk')
		post = Post.objects.get(pk=post_pk)
		form.instance.post = post
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('post-detail', kwargs={'pk': self.kwargs.get('pk')})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/comment_form.html'
	fields = ['content']

	def get_success_url(self):
		return reverse_lazy('post-detail', kwargs={'pk': self.get_object().post.pk})

	def test_func(self):
		comment = self.get_object()
		return comment.author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'blog/comment_confirm_delete.html'

	def get_success_url(self):
		return reverse_lazy('post-detail', kwargs={'pk': self.get_object().post.pk})

	def test_func(self):
		comment = self.get_object()
		return comment.author == self.request.user
