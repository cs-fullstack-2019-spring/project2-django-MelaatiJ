# Generated by Django 2.0.6 on 2019-03-17 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0005_auto_20190317_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rientrymodel',
            old_name='createDate',
            new_name='createdDate',
        ),
    ]
