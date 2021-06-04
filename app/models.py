from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    choices=models.ManyToManyField('Choice')
    voted_users=models.ManyToManyField(User)
    def __str__(self):
        return self.title

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    choice_image=models.ImageField(blank=True)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
