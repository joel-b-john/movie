# Generated by Django 3.2 on 2021-04-20 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='dese',
            new_name='desc',
        ),
    ]
