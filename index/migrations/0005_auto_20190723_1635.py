# Generated by Django 2.2.3 on 2019-07-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190723_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafeinformation',
            name='saclose',
        ),
        migrations.RemoveField(
            model_name='cafeinformation',
            name='saopen',
        ),
        migrations.RemoveField(
            model_name='cafeinformation',
            name='sunclose',
        ),
        migrations.RemoveField(
            model_name='cafeinformation',
            name='sunopen',
        ),
        migrations.AddField(
            model_name='cafeinformation',
            name='othertime',
            field=models.CharField(default='', max_length=500),
        ),
    ]