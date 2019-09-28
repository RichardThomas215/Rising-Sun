# Generated by Django 2.2.5 on 2019-09-28 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalView', '0007_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tasks',
        ),
        migrations.AddField(
            model_name='event',
            name='task_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task1', to='finalView.Task'),
        ),
        migrations.AddField(
            model_name='event',
            name='task_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task2', to='finalView.Task'),
        ),
        migrations.AddField(
            model_name='event',
            name='task_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task3', to='finalView.Task'),
        ),
        migrations.AddField(
            model_name='event',
            name='task_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task4', to='finalView.Task'),
        ),
        migrations.AddField(
            model_name='event',
            name='task_5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task5', to='finalView.Task'),
        ),
    ]