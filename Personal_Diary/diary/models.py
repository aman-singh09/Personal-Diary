from django.db import models

class Diary(models.Model):
	date = models.DateField(auto_now=False, auto_now_add=True)
	title = models.CharField(max_length = 30)
	content = models.TextField()
	mood = models.CharField(max_length = 10)
