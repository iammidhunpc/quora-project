# Generated by Django 2.0.5 on 2018-05-08 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0031_ans_que'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ans',
            old_name='que',
            new_name='ques',
        ),
    ]
