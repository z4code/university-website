# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('new/<int:pk>/', views.new, name='new'),
	path('news/', views.news, name='news'),
	path('event/<int:pk>/', views.event, name='event'),
	path('events/', views.events, name='events'),

	# USER AUTH.
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
]