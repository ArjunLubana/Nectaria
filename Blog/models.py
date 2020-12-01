from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	short_description = models.CharField(max_length=500)
	message = models.TextField()
	date_created = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)

	def __str__(self):
		return self.title