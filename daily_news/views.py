from django.http import HttpResponse
from .models import Topic, Keyword
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
	# here I am using generic view ListView to list all topics
	# for detail I could use DetailView - but had to adjust keywords then in return statment - topic.pk ???
	template_name = 'daily_news/index.html'
	context_object_name = 'latest_topic_list'

	def get_queryset(self):
		"""Return the last five published topics."""
		return Topic.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:5]


def detail(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	return render(request, 'daily_news/detail.html', {'topic': topic})


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
			'daily_news/detail.html',
			{'topic': topic, 'error_message': "You didn't provide any keyword."},
		)
	return redirect('daily_news:detail', topic_id=topic.id)


def description(request, topic_id):
	return HttpResponse(f"You're looking at descrition of topic {topic_id}")
