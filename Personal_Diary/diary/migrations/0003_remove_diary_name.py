# Generated by Django 3.0.8 on 2020-07-20 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_diary_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='name',
        ),
    ]
