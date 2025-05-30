from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='daily-news-home'),
	path('about/', views.about, name='daily-news-about'),
	path('topics/', views.topics, name='daily-news-topics'),
]
