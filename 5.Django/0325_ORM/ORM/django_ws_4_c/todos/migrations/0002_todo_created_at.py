# Generated by Django 4.2.11 on 2024-03-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
