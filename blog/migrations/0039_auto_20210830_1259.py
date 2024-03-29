# Generated by Django 3.1 on 2021-08-30 10:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20210814_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='maintext_translated',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('uncategorized', 'uncategorized')], default='uncategorized', max_length=200),
        ),
    ]
