from django.db import models
from Guest.models import  *
from MusicBand.models import *
from Freelancer.models import *
# Create your models here.

class tbl_bandbooking(models.Model):
    bandwork=models.ForeignKey(tbl_Bandworks,on_delete=models.CASCADE)
    booking_venue=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_fordate=models.DateField()
    booking_fortime=models.TimeField()
    booked_date=models.DateField(auto_now_add=True)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    booking_status=models.CharField(max_length=10,default=0)
    booking_amount=models.CharField(max_length=50,default=0)
    payment_status=models.CharField(max_length=10,default=0)

class tbl_SendComplaint(models.Model):
    SendComplaint_title=models.CharField(max_length=50)
    SendComplaint_content=models.CharField(max_length=50)

class tbl_SendFeedback(models.Model):
    SendFeedback_feedback=models.CharField(max_length=50)

class tbl_coursebooking(models.Model):
    course=models.ForeignKey(tbl_Course,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    cbooked_date=models.DateField(auto_now_add=True)
    cbooking_status=models.CharField(max_length=10,default=0)
    payment_status=models.CharField(max_length=10,default=0)

class tbl_complaint(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)
