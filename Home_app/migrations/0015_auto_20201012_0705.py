# Generated by Django 3.0.5 on 2020-10-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0014_quote_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.CharField(max_length=400),
        ),
    ]
