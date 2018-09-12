from django.db import models

class Quote(models.Model):
	category = models.CharField(max_length=25, null=True) 
	content = models.CharField(max_length=250, null=True)
	quoted_by = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.content[:80]