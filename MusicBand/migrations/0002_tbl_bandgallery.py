# Generated by Django 5.0.1 on 2024-03-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicBand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_BandGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BandGallery_caption', models.CharField(max_length=50)),
                ('BandGallery_files', models.FileField(upload_to='GalleryDoc/')),
            ],
        ),
    ]
