import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Keyword(models.Model):
	word = models.CharField(max_length=50, unique=True, null=False, blank=False)

	def __str__(self):  # pyright: ignore [reportIncompatibleMethodOverride]
		return self.word


class Topic(models.Model):
	name = models.CharField(max_length=50)
	max_news_per_day = models.IntegerField(
		default=0,  # pyright: ignore [reportArgumentType]
		help_text='Maximum number of news articles to reveive daily for this topic.',
		# TODO: add validation of max news
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
	keywords = models.ManyToManyField(Keyword, related_name='topics_using_this_keyword')
	created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)

	description = models.TextField(
		blank=True,
		null=True,
	)

	class Meta:
		unique_together = ('user', 'name')
		verbose_name = 'User Topic'
		verbose_name_plural = 'User Topics'
		ordering = ['user__username', '-created_at']

	def __str__(self):  # pyright: ignore [reportIncompatibleMethodOverride]
		return self.name

	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)
