# Generated by Django 4.2.2 on 2023-12-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('phone', models.IntegerField(null=True)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
