# Generated by Django 3.1.7 on 2021-04-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210403_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('mind over matter', 'mind over matter'), ('physical activity', 'physical activity'), ('uncategorized', 'uncategorized')], default='uncategorized', max_length=200),
        ),
    ]
