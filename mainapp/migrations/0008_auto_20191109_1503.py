# Generated by Django 2.2.5 on 2019-11-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20191109_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagename',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='imageurl',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
