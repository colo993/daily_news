import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from news.models import Topic


class TopicModelTest(TestCase):
	def test_was_published_recently_with_future_topic(self):
		"""was_published_recently() returns False for Topics whose pub_date is in the future."""
		time = timezone.now() + datetime.timedelta(days=30)
		future_topic = Topic(created_at=time)
		self.assertIs(future_topic.was_created_recently(), False)

	def test_was_published_recently_with_old_topic(self):
		"""was_published_recently() returns False for Topics whose pub_date is older than 1 day."""
		time = timezone.now() + datetime.timedelta(days=1, seconds=1)
		old_topic = Topic(created_at=time)
		self.assertIs(old_topic.was_created_recently(), False)

	def test_was_published_recently_with_recent_topic(self):
		"""was_published_recently() returns True for Topics whose pub_date is within the last day."""  # noqa: E501
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_topic = Topic(created_at=time)
		self.assertIs(recent_topic.was_created_recently(), True)


def create_topic(topic_name, days, user_name):
	"""Create a topic with the given 'topic_name' and created_at the given number of 'days' offset
	to now (negative for questions published in the past,
	positive for questions that have yet to be published).
	"""  # noqa:D205
	time = timezone.now() + datetime.timedelta(days=days)
	user = User.objects.create_user(username=user_name, password='password')
	return Topic.objects.create(name=topic_name, user=user, created_at=time)


class TopicIndexViewTest(TestCase):
	# Django convention, runs automatically and create a user
	def setUp(self):
		self.user = User.objects.create_user(username='user', password='Test123')

	def test_no_topics(self):
		"""If no questions exist, an appropriate message is displayed."""
		self.client.login(username='user', password='Test123')
		response = self.client.get(reverse('news:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No topics are available')
		self.assertQuerySetEqual(response.context['latest_topic_list'], [])

	def test_past_topic(self):
		self.client.login(username='user', password='Test123')
		topic = create_topic(topic_name='Past topic', days=-30, user_name='test_user')
		response = self.client.get(reverse('news:index'))
		self.assertQuerySetEqual(
			response.context['latest_topic_list'],
			[topic],
		)

	def test_future_topic(self):
		self.client.login(username='user', password='Test123')
		response = self.client.get(reverse('news:index'))
		self.assertContains(response, 'No topics are available')
		self.assertQuerySetEqual(
			response.context['latest_topic_list'],
			[],
		)

	def test_future_question_and_past_question(self):
		self.client.login(username='user', password='Test123')
		topic = create_topic(topic_name='Past topic', days=-30, user_name='test_user1')
		create_topic(topic_name='Future topic', days=30, user_name='test_user2')
		response = self.client.get(reverse('news:index'))
		self.assertQuerySetEqual(
			response.context['latest_topic_list'],
			[topic],
		)

	def test_two_past_questions(self):
		"""The questions index page may display multiple questions."""
		self.client.login(username='user', password='Test123')
		topic1 = create_topic(topic_name='Past topic 1.', days=-30, user_name='test_user1')
		topic2 = create_topic(topic_name='Past topic 2.', days=-5, user_name='test_user2')
		response = self.client.get(reverse('news:index'))
		self.assertQuerySetEqual(
			response.context['latest_topic_list'],
			[topic2, topic1],
		)

	def test_unathicated_user(self):
		"""User not logged in, so didn't get 200 response just was redirected."""
		response = self.client.get(reverse('news:index'))
		self.assertEqual(response.status_code, 302)
