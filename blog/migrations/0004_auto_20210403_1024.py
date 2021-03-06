# Generated by Django 3.1.7 on 2021-04-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210324_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Un-Publish')], default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Un-Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('immunity', 'immunity'), ('uncategorized', 'uncategorized')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Un-Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('physical activity', 'physical activity'), ('uncategorized', 'uncategorized')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.CharField(choices=[('immunity', 'immunity'), ('uncategorized', 'uncategorized')], default='', max_length=200),
        ),
    ]
