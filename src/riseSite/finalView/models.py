from django.db import models

class keyPlayer(models.Model):
    name = models.CharField(max_length=100, default="")
    position = models.CharField(max_length=100, default="")

class Task(models.Model):
    name = models.CharField(max_length=100, default="")
    key_player = models.OneToOneField(
        keyPlayer,
        on_delete=models.CASCADE,
        primary_key=True,
        default=''
    )
    deadline = models.DateField(null = True)
    notes = models.CharField(max_length=100, default="")

class Event(models.Model):
    name = models.CharField(max_length=100, default="")
    task_1 = models.ForeignKey(Task, related_name='task1', on_delete=models.CASCADE, null=True, blank=True)
    task_2 = models.ForeignKey(Task, related_name='task2', on_delete=models.CASCADE, null=True, blank=True)
    task_3 = models.ForeignKey(Task, related_name='task3', on_delete=models.CASCADE, null=True, blank=True)
    task_4 = models.ForeignKey(Task, related_name='task4', on_delete=models.CASCADE, null=True, blank=True)
    task_5 = models.ForeignKey(Task, related_name='task5', on_delete=models.CASCADE, null=True, blank=True)
