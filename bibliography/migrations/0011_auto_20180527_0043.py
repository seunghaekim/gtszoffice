# Generated by Django 2.0.5 on 2018-05-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0010_auto_20180526_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1527349385.7566302, max_length=20, unique=True),
        ),
    ]