# Generated by Django 3.1.7 on 2021-04-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20210424_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cardtype',
            field=models.IntegerField(choices=[(0, 'Big'), (1, 'Small')], default=0),
        ),
    ]
