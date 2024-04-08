from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.

class tbl_Course(models.Model):
    Course_details=models.CharField(max_length=50)
    Course_duration=models.CharField(max_length=50)
    Course_amount=models.CharField(max_length=50)
    Course_files=models.FileField(upload_to='courseDoc/')
    musicaltype=models.ForeignKey(tbl_Musicaltype,on_delete=models.CASCADE,null=True)
    freelancer=models.ForeignKey(tbl_FreelancerRegistration,on_delete=models.CASCADE,null=True)


class tbl_Gallery(models.Model):
    Gallery_caption=models.CharField(max_length=50)
    Gallery_files=models.FileField(upload_to='GllryDoc/')
    freelancer=models.ForeignKey(tbl_FreelancerRegistration,on_delete=models.CASCADE,null=True)