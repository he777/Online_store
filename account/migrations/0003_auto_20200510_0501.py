# Generated by Django 3.0.5 on 2020-05-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200509_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='account/img/fb79cc97-47e9-430b-8883-4ef6239d55b7/'),
        ),
    ]
