# Generated by Django 3.2.6 on 2021-08-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='News', max_length=100),
        ),
    ]
