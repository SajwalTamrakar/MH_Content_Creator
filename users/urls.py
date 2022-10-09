"""Define urls for users app"""

from django.urls import path, include

from. import views

app_name = "users"

urlpatterns = [
	#includes defaulth auth urls
	path('', include('django.contrib.auth.urls')),
	#Registration page url
	path('register/', views.register, name='register'),

]