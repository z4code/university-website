from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm
from . import models
from django.http import HttpResponse

# Home.
def home(request):
	news = models.New.objects.order_by('-updated_at')[:3]
	events = models.Event.objects.order_by('-updated_at')[:3]
	return render(request, 'main/home.htm', {'news': news, 'events': events})

# New.
def new(request, pk):
	new = models.New.objects.get(pk=pk)
	return render(request, 'main/new.htm', {'new': new})

# Logon.
def login_user(request):
	# Checking that the request status is POST.
	if request.method == 'POST':
		# Get username and password.
		username = request.POST['username']
		password = request.POST['password']
		user  = authenticate(request, username=username, password=password)
		# Checking that the user is not NONE.
		if user is not None:
			login(request, user)
			# Send a success message to the user.
			messages.success(request, ('You have successfully logged in!'))
			return redirect('university')
		else:
			# Send a warning message to the user.
			messages.warning(request, ('Invalid username or password. Please try again.'))
			return redirect('login')
	return render(request, 'main/login.htm')

# Logout.
def logout_user(request):
	logout(request)
	# Send an informational message to the user.
	messages.success(request, ('You have successfully logged out!'))
	return redirect('home')

# Register.
def register_user(request):
	'''View for user registration.'''

	# Checking that the request status is POST.
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		# Checking the validity of the request sent to the form.
		if form.is_valid():
			user = form.save()
			# User login.
			login(request, user)
			# Send a success message to the user.
			messages.success(request, ('Your account has been created successfully!'))
			return redirect('home')
	else:
		# If the form comes up empty.
		form = RegisterForm()
	return render(request, 'main/register.htm', {'form': form})

# Event.
def event(request, pk):
	return HttpResponse('Event!')

# News.
def news(request):
	news = models.New.objects.order_by('-updated_at')
	return render(request, 'main/news.htm', {'news': news})