# Generated by Django 2.2.5 on 2019-11-11 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_item_expired'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='expired',
            new_name='status',
        ),
    ]
