"""deinfing urls for contents app"""

from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	path('imptopics/', views.imptopics, name='imptopics'),
	path('imptopics/<int:topic_id>/', views.imptopic, name='imptopic'),
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	
]