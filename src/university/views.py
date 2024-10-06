from django.shortcuts import render, redirect
from django.contrib import messages

# Home.
def home(request):
	if request.user.is_authenticated:
		return render(request, 'university/home.htm', {})
	else:
		messages.warning(request, ('You are not logged in. Please login or register!'))
		return redirect('home')
