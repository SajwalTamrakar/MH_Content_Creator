from django import forms

from .models import ImprovisationTopic as it, ImprovisationEntry as ie


class ImprovisationTopicForm (forms.ModelForm):

	class Meta:

		model = it

		fields = ['title', 'key','scale','chords']
		labels = {'title': 'Title', 'key': 'Key', 'scale':'Scale','chords':'Chords'}

class ImprovisationEntryForm (forms.ModelForm):

	class Meta:

		model = ie

		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}