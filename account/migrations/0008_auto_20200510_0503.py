# Generated by Django 3.0.5 on 2020-05-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200510_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='account/img/034343ac-5c1e-45c5-800a-c098864e4f04/'),
        ),
    ]
