# Generated by Django 2.0.5 on 2018-05-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0030_auto_20180508_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='ans',
            name='que',
            field=models.CharField(default='unknwnquestion', max_length=100),
        ),
    ]
