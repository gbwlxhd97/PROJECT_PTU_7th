# Generated by Django 2.2.3 on 2019-07-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20190723_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeinformation',
            name='other',
            field=models.CharField(default='', editable=False, max_length=500),
        ),
    ]
