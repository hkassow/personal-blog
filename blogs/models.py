from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    update_date = models.DateTimeField('last updated')
    body = HTMLField()

    def __str__(self) -> str:
        return self.post_title

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = timezone.now()
        self.update_date = timezone.now()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        print('A post has been created or updated and this is its id:', self.id)

class Subscribers(models.Model):
    email = models.CharField(max_length=60)
    sub_date = models.DateTimeField('date subscribed')

    def save(self, *args, **kwargs):
        self.sub_date = timezone.now()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        

