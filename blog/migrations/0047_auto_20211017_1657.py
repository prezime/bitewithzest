# Generated by Django 3.1.7 on 2021-10-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20211016_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlang',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='postlang',
            name='custom_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postlang',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Un-Publish')], default=0),
        ),
        migrations.AddField(
            model_name='postlang',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
