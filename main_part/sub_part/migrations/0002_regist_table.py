# Generated by Django 4.0.3 on 2022-03-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regist_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('confrim_password', models.CharField(max_length=20)),
            ],
        ),
    ]