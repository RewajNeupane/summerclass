# Generated by Django 5.2.4 on 2025-07-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_blogs_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='blogs/products'),
        ),
    ]
