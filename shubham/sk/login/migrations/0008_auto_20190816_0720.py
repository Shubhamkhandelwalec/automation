# Generated by Django 2.2.4 on 2019-08-16 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20190814_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='isemail',
            new_name='isverified',
        ),
    ]
