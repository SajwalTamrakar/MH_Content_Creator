from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ImprovisationTopic(models.Model):
	"""This title of content of one song post for improvisation """

	text = models.CharField(max_length=500)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return string representation of the model"""
		return self.text


class ImprovisationEntry(models.Model):
	"""The content of each song improvisation post"""

	topic = models.ForeignKey(ImprovisationTopic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Improvisation entries'

	def __str__(self):
		"""Return a string representation of the model."""
		#if len(self.text) < 50:
		return self.text
		#else:
		#	return self.text[:50] + "..."
