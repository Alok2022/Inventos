# Generated by Django 4.0.3 on 2022-04-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0003_prod_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='device_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceName', models.CharField(max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('ProductId', models.CharField(max_length=20)),
                ('ManufacturingId', models.CharField(max_length=20)),
                ('ManufactureDate', models.DateField()),
                ('Comment', models.CharField(max_length=200)),
                ('CustomerHelpLine', models.CharField(max_length=20)),
                ('TotalProduct', models.CharField(max_length=500)),
            ],
        ),
    ]
