# Generated by Django 3.0.5 on 2020-05-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20200510_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='account/img/f56d3eb5-74c2-4885-b917-4fe500f59e2f/'),
        ),
    ]
