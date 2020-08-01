from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	date = models.DateField(auto_now=False, auto_now_add=True)
	title = models.CharField(max_length = 30)
	content = models.TextField()
	mood = models.CharField(max_length = 10)
