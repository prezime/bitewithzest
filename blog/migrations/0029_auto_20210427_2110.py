# Generated by Django 3.1.7 on 2021-04-27 21:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20210427_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AlterField(
            model_name='post',
            name='legend',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('Animal World', 'Animal World'), ('Mind over matter', 'Mind over matter'), ('Physical activity', 'Physical activity'), ('Plant World', 'Plant World'), ('uncategorized', 'uncategorized')], default='uncategorized', max_length=200),
        ),
    ]
