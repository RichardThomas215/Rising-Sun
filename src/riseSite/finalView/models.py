from django.db import models

class Issue(models.Model):
    name = models.CharField(max_length=100, default="")

class Event(models.Model):
    name = models.CharField(max_length=100, default="")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=False)

class Task(models.Model):
    name = models.CharField(max_length=100, default="")
    headline = models.TextField(max_length=100, default="")
    notes = models.TextField(max_length=250, default="")
    deadline = models.DateField(null = True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)

