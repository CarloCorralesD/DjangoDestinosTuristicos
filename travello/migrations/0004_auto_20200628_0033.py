# Generated by Django 3.0.7 on 2020-06-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20200628_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='.'),
        ),
    ]
