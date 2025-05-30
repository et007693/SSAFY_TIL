# Generated by Django 4.2.11 on 2024-03-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=10)),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('category_name', models.TextField()),
                ('category_id', models.IntegerField()),
                ('price', models.IntegerField()),
                ('fixed_price', models.BooleanField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
