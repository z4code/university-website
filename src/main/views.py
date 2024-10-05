from django.shortcuts import render
from . import models

# Home.
def home(request):
	news = models.New.objects.order_by('-created_at')[:3]
	return render(request, 'main/home.htm', {'news': news})

# New.
def new(request, pk):
	new = models.New.objects.get(id=pk)
	return render(request, 'main/new.htm', {'new': new})