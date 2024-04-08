# Generated by Django 5.0.1 on 2024-03-19 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_tbl_admin'),
        ('Freelancer', '0002_tbl_gallery'),
        ('Guest', '0011_delete_tbl_userregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_course',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_freelancerregistration'),
        ),
        migrations.AddField(
            model_name='tbl_course',
            name='musicaltype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_musicaltype'),
        ),
    ]