# Generated by Django 3.1.7 on 2021-04-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20210416_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='custom_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
