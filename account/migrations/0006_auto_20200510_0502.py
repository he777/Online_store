# Generated by Django 3.0.5 on 2020-05-10 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200510_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='account/img/3f564cc6-ee7e-41cf-8ff8-5fc0a603e95c/'),
        ),
    ]
