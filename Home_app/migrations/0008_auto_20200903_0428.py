# Generated by Django 3.0.5 on 2020-09-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0007_merge_20200903_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, choices=[('ACT', 'ACT'), ('NSW', 'NSW'), ('VIC', 'VIC'), ('SA', 'SA'), ('WA', 'WA'), ('NT', 'NT'), ('TAS', 'TAS')], default='ACT', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='suburb',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='address1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='postcode',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='state',
            field=models.CharField(blank=True, choices=[('ACT', 'ACT'), ('NSW', 'NSW'), ('VIC', 'VIC'), ('SA', 'SA'), ('WA', 'WA'), ('NT', 'NT'), ('TAS', 'TAS')], default='ACT', max_length=10),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='suburb',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tradie',
            name='travelDistance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]
