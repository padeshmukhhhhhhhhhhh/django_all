# Generated by Django 4.2.2 on 2024-01-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labels', models.CharField(max_length=300)),
                ('data', models.IntegerField()),
            ],
        ),
    ]