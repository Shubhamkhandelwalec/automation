# Generated by Django 2.2.4 on 2019-08-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190813_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='randomid',
            field=models.IntegerField(default=0, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tempregister',
            name='randomid',
            field=models.IntegerField(max_length=50, unique=True),
        ),
    ]
