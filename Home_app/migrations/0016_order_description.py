# Generated by Django 3.0.5 on 2020-10-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0015_auto_20201012_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
