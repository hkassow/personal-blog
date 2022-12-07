from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    update_date = models.DateTimeField('last updated', auto_now=True)
    post_body = HTMLField()

    def __str__(self) -> str:
        return self.post_title