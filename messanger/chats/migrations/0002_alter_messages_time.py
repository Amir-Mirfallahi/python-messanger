# Generated by Django 4.1.5 on 2023-01-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
