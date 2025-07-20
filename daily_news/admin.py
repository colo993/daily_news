from django.contrib import admin

from .models import Topic, Keyword

admin.site.register(Keyword)
admin.site.register(Topic)
