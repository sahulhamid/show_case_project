# Generated by Django 3.1.4 on 2020-12-27 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201227_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='image',
            field=models.ImageField(default=None, upload_to='users_post'),
        ),
    ]