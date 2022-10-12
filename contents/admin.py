from django.contrib import admin

# Register your models here.

from . models import ImprovisationTopic, ImprovisationEntry, Fretboard

admin.site.register(ImprovisationTopic)
admin.site.register(ImprovisationEntry)
admin.site.register(Fretboard)
