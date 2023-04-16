from django.contrib import admin
from .models import Support


class SupportTicketAdmin(admin.ModelAdmin):
    list_filter = ('status', 'owner')
    list_display = ('id', 'title', 'status', 'owner', 'issue', 'updated_at')
    search_fields = ['title', 'status']
    actions = ['status_in_progress', 'status_on_hold', 'status_resolved']

    def status_in_progress(self, request, queryset):
        queryset.update(status='in_progress')

    def status_on_hold(self, request, queryset):
        queryset.update(status='on_hold')

    def status_resolved(self, request, queryset):
        queryset.update(status='resolved')


admin.site.register(Support, SupportTicketAdmin)
