# Generated by Django 2.0.6 on 2019-03-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0002_auto_20190317_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikientrymodel',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
