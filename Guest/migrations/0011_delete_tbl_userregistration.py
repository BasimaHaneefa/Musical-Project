# Generated by Django 5.0.1 on 2024-03-09 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0010_alter_tbl_freelancerregistration_freelancerregistration_vstatus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_UserRegistration',
        ),
    ]