# Generated by Django 3.1.7 on 2021-04-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_post_custom_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='custom_date',
            field=models.DateTimeField(blank=True),
        ),
    ]