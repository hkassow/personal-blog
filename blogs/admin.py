from django.contrib import admin

from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'post_title', 'post_body']
admin.site.register(Post, PostAdmin)