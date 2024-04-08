from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import tbl_district,tbl_place
# Create your views here.
def MusicalBandRegistration(request):
    data=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('placedrp'))
        tbl_MusicalBandRegistration.objects.create(MusicalBandRegistration_name=request.POST.get('txt_musicalbandname'),MusicalBandRegistration_email=request.POST.get('txt_musicalbandemail'),MusicalBandRegistration_contact=request.POST.get('txt_musicalbandcontact'),MusicalBandRegistration_address=request.POST.get('txt_musicalbandaddress'),place=place,MusicalBandRegistration_logo=request.FILES.get('Logo'),MusicalBandRegistration_proof=request.FILES.get('Proof'),MusicalBandRegistration_password=request.POST.get('txt_musicalbandpassword'))
        return render(request,"Guest/MusicalBandRegistration.html",{"District":data})
    else:
        return render(request,"Guest/MusicalBandRegistration.html",{"District":data})


def FreelancerRegistration(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('placedrp'))
        tbl_FreelancerRegistration.objects.create(FreelancerRegistration_name=request.POST.get('txt_freelancername'),FreelancerRegistration_contact=request.POST.get('txt_freelancercontact'),FreelancerRegistration_email=request.POST.get('txt_freelanceremail'),FreelancerRegistration_address=request.POST.get('txt_freelanceraddress'),place=place,FreelancerRegistration_photo=request.FILES.get('Photo'),FreelancerRegistration_proof=request.FILES.get('Proof'),FreelancerRegistration_password=request.POST.get('txt_freelancerpassword'))
        return render(request,"Guest/FreelancerRegistration.html",{"District":district})
    else:
        return render(request,"Guest/FreelancerRegistration.html",{"District":district})

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("disd"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})


def Login(request):
    if request.method=="POST":
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")
        admincount=tbl_admin.objects.filter(Login_Email=Email,Login_Password=Password).count()
        newusercount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        freelancercount=tbl_FreelancerRegistration.objects.filter(FreelancerRegistration_email=Email,FreelancerRegistration_password=Password,FreelancerRegistration_vstatus=1).count()
        musicbandcount=tbl_MusicalBandRegistration.objects.filter(MusicalBandRegistration_email=Email,MusicalBandRegistration_password=Password,MusicalBandRegistration_vstatus=1).count()
        if newusercount>0:
           userdata=tbl_user.objects.get(user_email=Email,user_password=Password)
           request.session["uid"]=userdata.id
           return redirect("User:homepage")
        elif freelancercount>0:
           freelancerdata=tbl_FreelancerRegistration.objects.get(FreelancerRegistration_email=Email,FreelancerRegistration_password=Password,FreelancerRegistration_vstatus=1)
           request.session["fid"]=freelancerdata.id
           return redirect("Freelancer:homepage")
        elif musicbandcount>0:
           musicbanddata=tbl_MusicalBandRegistration.objects.get(MusicalBandRegistration_email=Email,MusicalBandRegistration_password=Password,MusicalBandRegistration_vstatus=1)
           request.session["mid"]=musicbanddata.id
           return redirect("musicband:homepage")
        elif admincount>0:
            admindata=tbl_admin.objects.get(Login_Email=Email,Login_Password=Password)
            request.session["adid"]=admindata.id
            return redirect("webadmin:AdminHome")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email or Password"})
    else:
        return render(request,"Guest/Login.html")

def Index(request):
     return render(request,"Guest/Index.html")
