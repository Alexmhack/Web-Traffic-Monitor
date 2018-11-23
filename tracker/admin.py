from django.contrib import admin

from .models import Page, Session

@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
	list_display = ('name', 'session', 'first_visit', 'visits')
	list_display_links = ('session', 'visits')
	list_editable = ('name',)
	search_fields = ('name', 'visits')
	list_filter = ('name',)


@admin.register(Session)
class SessionModelAdmin(admin.ModelAdmin):
	list_display = ('country', 'city', 'browser')
	search_fields = ('country', 'city', 'browser', 'os')
	list_filter = ('country', 'browser', 'os')
