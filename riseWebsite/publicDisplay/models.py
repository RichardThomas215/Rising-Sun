from django.db import models

# Create your models here.
class Event(models.Model):
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    key_player_1 = models.OneToOneField(
        keyPlayers,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    key_player_2 = models.OneToOneField(
        keyPlayers,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    key_player_3 = models.OneToOneField(
        keyPlayers,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    deadline = models.DateField(null = True)
    notes = models.CharField(max_length=100)

class keyPlayers(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Issue(models.Model):
    issueName = models.CharField(max_length=100)
    Description = models.CharField(max_lenght=100)