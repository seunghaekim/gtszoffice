# Generated by Django 2.0.5 on 2018-05-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0015_auto_20180527_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1527357676.452215, max_length=20, unique=True),
        ),
    ]