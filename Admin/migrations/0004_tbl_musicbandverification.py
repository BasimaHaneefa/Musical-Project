# Generated by Django 5.0.1 on 2024-02-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_place_dist'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_MusicbandVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Musicband_Verification', models.CharField(max_length=100)),
            ],
        ),
    ]
