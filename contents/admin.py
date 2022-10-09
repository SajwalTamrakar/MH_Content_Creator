from django.contrib import admin

# Register your models here.

from . models import ImprovisationTopic, ImprovisationEntry

admin.site.register(ImprovisationTopic)
admin.site.register(ImprovisationEntry)

