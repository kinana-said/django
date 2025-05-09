from django.db import models

# Create your models here.
#Guest__Movie__Resevation
class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    hall = models.DateField()

class Guest(models.Model):

  name = models.CharField(max_length=30)
  mobile =models.CharField(max_length=30)

class Resevation(models.Model):
   guest = models.ForeignKey(Guest,related_name='Resevation',on_delete=models.CASCADE)
   movie = models.ForeignKey(Movie,related_name='Resevation',on_delete=models.CASCADE )