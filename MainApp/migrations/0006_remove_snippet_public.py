# Generated by Django 4.1.7 on 2024-07-26 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_snippet_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='public',
        ),
    ]
