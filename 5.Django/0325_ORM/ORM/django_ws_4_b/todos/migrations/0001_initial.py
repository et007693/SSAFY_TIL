# Generated by Django 4.2.11 on 2024-03-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('is_completed', models.BooleanField()),
            ],
        ),
    ]
