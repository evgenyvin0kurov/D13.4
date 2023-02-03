# Generated by Django 4.0.4 on 2022-06-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_alter_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(related_name='posts', through='newsapp.PostCategory', to='newsapp.category'),
        ),
    ]
