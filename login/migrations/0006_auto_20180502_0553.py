# Generated by Django 2.0.4 on 2018-05-02 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20180430_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='studid',
            new_name='sid',
        ),
    ]
