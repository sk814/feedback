from django.contrib import admin
from .models import Feedback

class FeedabackAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Feedback, FeedabackAdmin)

