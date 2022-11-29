from django.contrib import admin

from .models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'details', 'date')

    class Meta:
        model = Feedback

admin.site.register(Feedback, FeedbackAdmin)