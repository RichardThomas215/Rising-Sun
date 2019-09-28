# Generated by Django 2.2.5 on 2019-09-28 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalView', '0003_auto_20190928_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='key_player_1',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='finalView.keyPlayer'),
        ),
        migrations.AlterField(
            model_name='keyplayer',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='keyplayer',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]