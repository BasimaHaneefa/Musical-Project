from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=100)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)
class tbl_subcategory(models.Model):
    Subcategory_name=models.CharField(max_length=100)
class tbl_complainttype(models.Model):
    ComplaintType_name=models.CharField(max_length=100)
class tbl_Musicaltype(models.Model):
    Musical_type=models.CharField(max_length=100)

class tbl_admin(models.Model):
    Login_Email=models.CharField(max_length=100)
    Login_Password=models.CharField(max_length=100)