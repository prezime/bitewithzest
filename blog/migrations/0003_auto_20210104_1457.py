# Generated by Django 3.1 on 2021-01-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cardtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cardtype',
            field=models.IntegerField(choices=[(0, 'Big'), (1, 'Small')], default=0),
        ),
    ]
