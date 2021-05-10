# Generated by Django 3.2 on 2021-05-02 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_intouch_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intouch',
            old_name='timestamp',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='intouch',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]