# Generated by Django 5.0.1 on 2024-03-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_rename_dist_tbl_place_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login_Email', models.CharField(max_length=100)),
                ('Login_Password', models.CharField(max_length=100)),
            ],
        ),
    ]
