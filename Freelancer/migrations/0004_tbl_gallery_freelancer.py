# Generated by Django 5.0.1 on 2024-03-19 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0003_tbl_course_freelancer_tbl_course_musicaltype'),
        ('Guest', '0011_delete_tbl_userregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_gallery',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_freelancerregistration'),
        ),
    ]
