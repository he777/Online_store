# Generated by Django 3.0.5 on 2020-05-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200510_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='account/img/6ec2d97c-abad-4d65-87ec-4fcb45211e29/'),
        ),
    ]
