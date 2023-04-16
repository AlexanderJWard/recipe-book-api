from django.contrib import admin
from .models import Support


class SupportTicketAdmin(admin.ModelAdmin):
    list_filter = ('status', 'owner')
    list_display = ('id', 'title', 'status', 'owner', 'issue', 'updated_at')
    search_fields = ['title', 'status']


admin.site.register(Support, SupportTicketAdmin)
