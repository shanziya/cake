# Generated by Django 3.2.11 on 2022-01-14 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake_shop', '0003_auto_20220112_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='img',
        ),
    ]
