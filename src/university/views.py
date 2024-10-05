from django.shortcuts import render

# Home.
def home(request):
	return render(request, 'university/home.htm', {})
