# Generated by Django 3.0.4 on 2020-03-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200322_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default-post.jpg', upload_to='post_pics'),
        ),
    ]
