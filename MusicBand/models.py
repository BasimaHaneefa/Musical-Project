from django.db import models
from Guest.models import *
# Create your models here.

class tbl_Bandworks(models.Model):
    Bandworks_details=models.CharField(max_length=50)
    Bandworks_files=models.FileField(upload_to='workDoc/')
    musicaltype=models.ForeignKey(tbl_Musicaltype,on_delete=models.CASCADE,null=True)
    musicband=models.ForeignKey(tbl_MusicalBandRegistration,on_delete=models.CASCADE,null=True)
   
class tbl_BandGallery(models.Model):
    BandGallery_caption=models.CharField(max_length=50)
    BandGallery_files=models.FileField(upload_to='GalleryDoc/')
    bandwork=models.ForeignKey(tbl_Bandworks,on_delete=models.CASCADE,null=True)
