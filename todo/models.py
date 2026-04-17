from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task (models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    description = models.TextField(max_length=300,null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_updation = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"your {self.title} is {self.complete}"
    