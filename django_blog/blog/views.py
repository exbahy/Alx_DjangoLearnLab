from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

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
