# Generated by Django 3.1.4 on 2020-12-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
