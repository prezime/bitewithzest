# Generated by Django 3.1.7 on 2021-04-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210416_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='custom_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]