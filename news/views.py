from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import generic

from .models import Keyword, Topic


class IndexView(LoginRequiredMixin, generic.ListView):
	# here I am using generic view ListView to list all topics
	# for detail I could use DetailView - but had to adjust keywords then in return statment - topic.pk ???
	template_name = 'news/index.html'
	context_object_name = 'latest_topic_list'
	redirect_field_name = '/bla/'

	def get_queryset(self):
		"""Return the last five published topics."""
		return Topic.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:5]


def detail(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	return render(request, 'news/detail.html', {'topic': topic})


def keywords(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	try:
		# figuret out how to prevent from adding empty strings and spaces to keyword
		# to insert the same keyword for different topic first check if it is already in the databased
		# and then create it if doesn't exists or else just add it to Topic
		inserted_keyword = request.POST.get('my_keyword')
		keyword = Keyword(word=inserted_keyword)
		keyword.save()
		topic.keywords.add(keyword)
	except:
		return render(
			request,
			'news/detail.html',
			{'topic': topic, 'error_message': "You didn't provide any keyword."},
		)
	return redirect('news:detail', topic_id=topic.id)


def description(request, topic_id):
	return HttpResponse(f"You're looking at descrition of topic {topic_id}")
