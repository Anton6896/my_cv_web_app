# Generated by Django 3.2 on 2021-05-11 11:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210503_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='languages',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='personal_quality',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]