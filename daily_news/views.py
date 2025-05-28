from django.shortcuts import render


def home(request):
	numbers = list(range(1, 11))
	context = {'numbers': numbers}
	return render(request, 'daily_news/home.html', context=context)


def about(request):
	return render(request, 'daily_news/about.html', context={'title': 'About'})
