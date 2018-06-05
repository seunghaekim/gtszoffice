# Generated by Django 2.0.5 on 2018-06-03 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0001_initial'),
        ('photo', '0002_auto_20180527_1636'),
        # ('bibliography', '0002_remove_book_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='images',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='photo.Gallery'),
        ),
    ]