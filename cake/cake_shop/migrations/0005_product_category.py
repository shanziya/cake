# Generated by Django 3.2.11 on 2022-01-15 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_shop', '0004_rename_image_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='cake_shop.category'),
            preserve_default=False,
        ),
    ]
