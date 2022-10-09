from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

from . models import ImprovisationTopic as it, ImprovisationEntry as ie
from .forms import ImprovisationTopicForm as itf, ImprovisationEntryForm as ief

# Create your views here.

def index(request):

	return render(request, 'contents/index.html')


@login_required
def imptopics(request):
	"""To show the list of all topics"""

	topics = it.objects.filter(owner=request.user).order_by('date_added') #get the list of topics for current user
	context = {'topics':topics}

	return render (request, 'contents/imptopics.html', context)

@login_required
def imptopic(request, topic_id):
	"""Shows topic details with its entries"""

	topic = it.objects.get(id=topic_id)
	if request.user != topic.owner:
		raise Http404
	entries = topic.improvisationentry_set.all().order_by('date_added')
	context = {'topic':topic, 'entries': entries}

	return render (request, 'contents/imptopic.html', context)


@login_required
def new_topic(request):
	"""Adding a new topic for improivsation"""

	if request.method != 'POST':
		"""if they are not posting or submitting the data"""
		form = itf() #show a blank form
	else:
		form = itf(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('contents:imptopics')

	#Display a blank invalid form	
	context = {'form':form}

	return render(request, 'contents/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

	topic = it.objects.get(id=topic_id)

	if request.method != 'POST':
		form =ief()
	else:
		form = ief(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('contents:imptopic', topic_id=topic_id)

	context = {'topic':topic, 'form': form}

	return render(request, 'contents/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):

	entry = ie.objects.get(id=entry_id)
	topic = entry.topic

	if topic.owner != request.user:
		raise Http404
		
	if request.method != 'POST':
		form = ief(instance=entry)
	else:
		form = ief(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('contents:imptopic', topic_id=topic.id)

	context = {'entry':entry, 'topic':topic, 'form': form}

	return render(request, 'contents/edit_entry.html', context)





















