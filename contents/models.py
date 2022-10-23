from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User
# Create your models here.

keys = (
	('a', 'A'),
	('a#', 'A#'),
	('b', 'B'),
	('c', 'C'), 
	('c#', 'C#'),
	('d', 'D'),
	('d#', 'D#'),
	('e', 'E'),
	('f', 'F'),
	('f#', 'F#'),
	('g', 'G'),
	('g#', 'G#'), 
)


scales = (
	('major', 'Major'),
	('minor', 'Minor'),
	('melodic', 'Melodic'),
	('harmonic', 'Harmonic'),  
)

class ImprovisationTopic(models.Model):
	"""This title of content of one song post for improvisation """

	title = models.CharField(max_length=500)
	key = models.CharField(max_length=500, choices=keys, default='C Major')
	scale = models.CharField(max_length=500, choices=scales, default='Major')
	chords = JSONField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return string representation of the model"""
		return self.title


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



class Fretboard(models.Model):
	"""the collection of images from fretboardgtr"""
	name = models.CharField(max_length=500)
	dominant = models.ImageField(blank=True, upload_to="media")
	dominant4 = models.ImageField(blank=True, upload_to="media")
	frets = models.ImageField(blank=True, upload_to="media")
	pentatonic = models.ImageField(blank=True, upload_to="media")	
	def __str__(self):
		"""Return string representation of the model"""
		return self.name




