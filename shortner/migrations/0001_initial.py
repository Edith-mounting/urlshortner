# Generated by Django 4.0.4 on 2022-04-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000)),
                ('uuid', models.CharField(max_length=10)),
            ],
        ),
    ]
