# Generated by Django 2.0.4 on 2018-05-03 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20180503_0550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rollno',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sid',
        ),
        migrations.AlterField(
            model_name='quest',
            name='logid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Logs'),
        ),
    ]
