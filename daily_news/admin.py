from django.contrib import admin

from .models import Topic, Keyword


class TopicAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['name']}), ('Date information', {'fields': ['created_at']})]
	list_display = ['name', 'created_at', 'was_created_recently']
	list_filter = ['created_at']
	search_fields = ['name']

class KeywordAdmin(admin.ModelAdmin):
	search_fields = ['word']


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Topic, TopicAdmin)
