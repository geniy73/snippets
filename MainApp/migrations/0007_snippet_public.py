# Generated by Django 4.1.7 on 2024-07-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_remove_snippet_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
