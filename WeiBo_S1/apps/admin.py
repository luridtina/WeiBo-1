from django.contrib import admin
from apps.models import Weibo, Topic, Category, Comment, Tags, UserProfile

# Register your models here.

admin.site.register(Weibo)
admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tags)
admin.site.register(UserProfile)
