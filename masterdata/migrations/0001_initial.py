# Generated by Django 4.1.5 on 2023-01-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='starmaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(max_length=200)),
                ('moment', models.CharField(max_length=200)),
                ('chat', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=200)),
            ],
        ),
    ]
