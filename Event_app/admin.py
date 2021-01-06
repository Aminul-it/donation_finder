from django.contrib import admin
from Event_app.models import event,Comment,Like

# Register your models here.
admin.site.register(event)
admin.site.register(Comment)
admin.site.register(Like)
