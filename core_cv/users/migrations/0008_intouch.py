# Generated by Django 3.2 on 2021-05-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='InTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
