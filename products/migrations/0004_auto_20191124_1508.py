# Generated by Django 2.2.5 on 2019-11-24 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191124_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='item',
            new_name='item_name',
        ),
    ]
