# Generated by Django 2.2.5 on 2019-09-28 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalView', '0004_auto_20190928_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='key_player_1',
            new_name='key_player',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.CharField(default='', max_length=100),
        ),
    ]
