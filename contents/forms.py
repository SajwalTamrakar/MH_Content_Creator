from django import forms

from .models import ImprovisationTopic as it, ImprovisationEntry as ie

class ImprovisationTopicForm (forms.ModelForm):

	class Meta:

		model = it

		fields = ['text']
		label = {'text': ''}

class ImprovisationEntryForm (forms.ModelForm):

	class Meta:

		model = ie

		fields = ['text']
		label = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}