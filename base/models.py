from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # relationship between message and room if a room get deleted the message get's deleted
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null=True = the database can have an instance with blank description
    # participants
    updated = models.DateTimeField(auto_now=True) # every time you call the method a timestamp is created
    created = models.DateTimeField(auto_now_add=True) # on creation timestamp

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # relationship between message and room if a room get deleted the message get's deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # every time you call the method a timestamp is created
    created = models.DateTimeField(auto_now_add=True) # on creation timestamp

    def __str__(self):
        return self.body[0:50]