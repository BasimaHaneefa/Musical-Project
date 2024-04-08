# Generated by Django 4.2.7 on 2024-03-27 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0011_delete_tbl_userregistration'),
        ('Freelancer', '0004_tbl_gallery_freelancer'),
        ('User', '0004_tbl_bandbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_coursebooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbooked_date', models.DateField(auto_now_add=True)),
                ('cbooking_status', models.CharField(default=0, max_length=10)),
                ('payment_status', models.CharField(default=0, max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Freelancer.tbl_course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
