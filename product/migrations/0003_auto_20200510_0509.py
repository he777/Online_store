# Generated by Django 3.0.5 on 2020-05-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_active',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(default=None, max_length=1000),
        ),
    ]
