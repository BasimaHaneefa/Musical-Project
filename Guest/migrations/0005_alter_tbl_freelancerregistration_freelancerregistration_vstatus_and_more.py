# Generated by Django 5.0.1 on 2024-02-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_freelancerregistration_freelancerregistration_vstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_freelancerregistration',
            name='FreelancerRegistration_vstatus',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_musicalbandregistration',
            name='MusicalBandRegistration_vstatus',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
    ]