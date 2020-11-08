from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    content = models.TextField(blank=True, null=True)


    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("article_detail_view", kwargs ={"id": self.id})