from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
	#Register a new user"
	if request.method != 'POST':
		#Registration form
		form = UserCreationForm()
	else:
		#Process completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#log the user in and redirect to home page
			login(request, new_user)
			return redirect('contents:index')

	#display blank or invalid form
	context={'form':form}
	return render(request, 'registration/register.html', context)