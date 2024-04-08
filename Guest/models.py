from django.db import models
from Admin.models import *

# Create your models here.
class tbl_MusicalBandRegistration(models.Model):
    MusicalBandRegistration_name=models.CharField(max_length=50,null=True)
    MusicalBandRegistration_email=models.CharField(max_length=50,null=True)
    MusicalBandRegistration_contact=models.CharField(max_length=50,null=True)
    MusicalBandRegistration_address=models.CharField(max_length=50,null=True)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)
    MusicalBandRegistration_logo=models.FileField(upload_to='BandDoc/',null=True)
    MusicalBandRegistration_proof=models.FileField(upload_to='BandDoc/',null=True)
    MusicalBandRegistration_password=models.CharField(max_length=50,null=True)
    MusicalBandRegistration_vstatus=models.CharField(max_length=10,default=0)

class tbl_FreelancerRegistration(models.Model):
    FreelancerRegistration_name=models.CharField(max_length=50,null=True)
    FreelancerRegistration_contact=models.CharField(max_length=50,null=True)
    FreelancerRegistration_email=models.CharField(max_length=50,null=True)
    FreelancerRegistration_address=models.CharField(max_length=50,null=True)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)
    FreelancerRegistration_photo=models.FileField(upload_to='FreeDoc/',null=True)
    FreelancerRegistration_proof=models.FileField(upload_to='FreeDoc/',null=True)
    FreelancerRegistration_password=models.CharField(max_length=50,null=True)
    FreelancerRegistration_vstatus=models.CharField(max_length=10,default=0,null=True)



class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
   