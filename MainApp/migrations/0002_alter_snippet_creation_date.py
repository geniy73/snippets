# Generated by Django 4.1.7 on 2024-07-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]