from django.db import models
from django import views

# Create your models here.
from django.urls import reverse



class City(models.Model):
    name = models.CharField(max_length=25, unique=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("weather_detail", kwargs ={"id": self.id})





    class Meta:
        verbose_name_plural = 'cities'

