# Generated by Django 4.1 on 2022-08-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='lang',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
