from django.db import models
from django.utils import timezone

class Quote(models.Model):
	category = models.CharField(max_length=25, null=True) 
	content = models.CharField(max_length=250, null=True)
	quoted_by = models.CharField(max_length=50, null=True)
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.content