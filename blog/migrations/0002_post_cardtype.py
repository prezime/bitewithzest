# Generated by Django 3.1.1 on 2020-10-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cardtype',
            field=models.IntegerField(choices=[(0, 'big'), (1, 'small')], default=0),
        ),
    ]
