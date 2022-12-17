from django.contrib import admin

from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title', 'body']
admin.site.register(Post, PostAdmin)