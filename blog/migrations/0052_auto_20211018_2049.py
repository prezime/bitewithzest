# Generated by Django 3.1.7 on 2021-10-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_auto_20211018_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlang',
            name='slug',
            field=models.SlugField(editable=False, max_length=200),
        ),
    ]
