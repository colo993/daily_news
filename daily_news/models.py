from django.db import models


class Topic(models.Model):
	name = models.CharField(max_length=20)
	target_words = models.CharField(max_length=100)
	amount_of_news = models.IntegerField(default=1) # pyright: ignore [reportArgumentType]
	created_at = models.DateTimeField('creation date')
	topic_description = models.CharField(max_length=200)
