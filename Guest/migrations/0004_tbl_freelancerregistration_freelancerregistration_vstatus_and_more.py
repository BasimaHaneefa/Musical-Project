# Generated by Django 5.0.1 on 2024-02-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_freelancerregistration_tbl_userregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_freelancerregistration',
            name='FreelancerRegistration_vstatus',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tbl_musicalbandregistration',
            name='MusicalBandRegistration_vstatus',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
