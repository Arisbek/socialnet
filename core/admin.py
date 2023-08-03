from django.contrib import admin
from .models import Profile, Post, Category,SavedPost,Short
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SavedPost)
admin.site.register(Short)