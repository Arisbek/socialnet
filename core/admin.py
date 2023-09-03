from django.contrib import admin
from .models import Profile, Post, Category,SavedPosts,Short,Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SavedPosts)
admin.site.register(Short)
admin.site.register(Comment)