from __future__ import unicode_literals

from django.db import models
#from django.forms import forms
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField()
    
    class Admin:
        list_display=('title','date')
        list_filter=('title')
        ordering=('date',)
        search_fields=('title',)
        
    def __unicode__(self):
        return self.title
