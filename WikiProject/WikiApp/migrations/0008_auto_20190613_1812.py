# Generated by Django 2.0.6 on 2019-06-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0007_auto_20190613_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rientrymodel',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='wikientrymodel',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
