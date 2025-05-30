from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
	topic_name = models.CharField(max_length=100)
	amount = models.IntegerField()
	language = models.CharField(max_length=100)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.topic_name
