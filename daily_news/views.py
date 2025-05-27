from django.shortcuts import render


posts = [
	{
		'author': 'Joe Doe',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'August 20, 2024',
	},
	{
		'author': 'Joe Doe',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'August 20, 2024',
	},
]


def home(request):
	context = {'posts': posts}
	return render(request, 'daily_news/home.html', context=context)


def about(request):
	return render(request, 'daily_news/about.html', context={'title': 'About'})
