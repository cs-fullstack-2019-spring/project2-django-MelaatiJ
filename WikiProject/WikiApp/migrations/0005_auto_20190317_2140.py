# Generated by Django 2.0.6 on 2019-03-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0004_auto_20190317_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rientrymodel',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]