# Generated by Django 3.1.7 on 2021-10-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_categorylang'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorylang',
            name='lang',
            field=models.CharField(choices=[('de', 'German'), ('en', 'English')], default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='categorylang',
            name='description',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='categorylang',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200),
        ),
    ]
