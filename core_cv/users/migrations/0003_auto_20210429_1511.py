# Generated by Django 3.2 on 2021-04-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210429_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='personal_quality',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]