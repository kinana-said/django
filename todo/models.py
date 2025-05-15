from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
   user = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
   title = models.CharField(max_length=24)
   description= models.TextField(max_length=255,blank=True)
   completed=models.BooleanField(default=False)
   created_at=models.DateTimeField(auto_now_add=True)


   def __str__(self):
     return self.title
   
