from django.urls import path

from . import views

app_name = 'daily_news'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:topic_id>/', views.detail, name='detail'),
	path('<int:topic_id>/keywords', views.keywords, name='keywords'),
	path('<int:topic_id>/description', views.description, name='description'),
]
