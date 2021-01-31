# Generated by Django 3.1 on 2021-01-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_titleplus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=200),
        ),
    ]
