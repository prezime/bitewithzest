# Generated by Django 3.1.7 on 2021-04-23 16:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210418_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='intro1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='outro',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='preparationtext',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
