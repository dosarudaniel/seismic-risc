# Generated by Django 2.2.4 on 2019-09-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('map_app', '0007_auto_20190916_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='nr_sector',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
