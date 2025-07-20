from django.http import HttpResponse
from .models import Topic, Keyword
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
	latest_topic_list = Topic.objects.order_by('-created_at')[:5]
	context = {'latest_topic_list': latest_topic_list}
	return render(request, 'daily_news/index.html', context)


def detail(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	return render(request, 'daily_news/detail.html', {'topic': topic})


def keywords(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	try:
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
