# Generated by Django 3.0.4 on 2020-03-22 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
