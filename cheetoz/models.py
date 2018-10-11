from __future__ import unicode_literals

from django.db import models

# Create your models here.

class cheetoz(models.Model):
	phonenumber = models.CharField(max_length=50)
	score = models.IntegerField(max_length=50)
