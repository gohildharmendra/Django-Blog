# Generated by Django 3.1.5 on 2021-05-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20210512_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
