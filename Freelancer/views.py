from django.shortcuts import render,redirect
from Guest.models import *
from Freelancer.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"Freelancer/HomePage.html")

def my_pro(request):
    data=tbl_FreelancerRegistration.objects.get(id=request.session["fid"])
    return render(request,"Freelancer/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_FreelancerRegistration.objects.get(id=request.session["fid"])
    if request.method=="POST":
        prodata.FreelancerRegistration_name=request.POST.get('txtname')
        prodata.FreelancerRegistration_contact=request.POST.get('txtcon')
        prodata.FreelancerRegistration_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Freelancer/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Freelancer/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_FreelancerRegistration.objects.filter(id=request.session["fid"],FreelancerRegistration_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                Freelancerdata=tbl_FreelancerRegistration.objects.get(id=request.session["fid"],FreelancerRegistration_password=request.POST.get('txtcurpass'))
                Freelancerdata.FreelancerRegistration_password=request.POST.get('txtnewpass')
                Freelancerdata.save()
                return render(request,"Freelancer/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Freelancer/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Freelancer/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Freelancer/ChangePassword.html")

def Course(request):
    prodata=tbl_FreelancerRegistration.objects.get(id=request.session["fid"])
    data=tbl_Musicaltype.objects.all()
    cdata=tbl_Course.objects.filter(freelancer=prodata)
    if request.method=="POST":
        seltype=tbl_Musicaltype.objects.get(id=request.POST.get("typedrp"))
        tbl_Course.objects.create(Course_details=request.POST.get("txt_details"),
                                 Course_duration=request.POST.get("txt_duration"),
                                 Course_amount=request.POST.get("txt_amount"),
                                 Course_files=request.FILES.get("files"),
                                 musicaltype=seltype,
                                 freelancer=prodata)
        return redirect("Freelancer:Course")
    else:
        return render(request,"freelancer/Course.html",{'data':data,'cdata':cdata})

def delcourse(request,did):
    tbl_Course.objects.get(id=did).delete()
    return redirect("Freelancer:Course")

def Gallery(request):
    prodata=tbl_FreelancerRegistration.objects.get(id=request.session["fid"])
    data=tbl_Gallery.objects.filter(freelancer=prodata)
    if request.method=="POST":
        tbl_Gallery.objects.create(Gallery_caption=request.POST.get("txt_gallerycaption"),
                                    Gallery_files=request.FILES.get("files"),
                                    freelancer=prodata)
        return redirect("Freelancer:Gallery")
    else:
        return render(request,"freelancer/Gallery.html",{'data':data})

def delgallery(request,did):
    tbl_Gallery.objects.get(id=did).delete()
    return redirect("Freelancer:Gallery")


def ViewCourseBooking(request):
    prodata=tbl_FreelancerRegistration.objects.get(id=request.session["fid"])
    data=tbl_coursebooking.objects.filter(course__freelancer=prodata)
    return render(request,"freelancer/ViewCourseBooking.html",{'data':data})


def AcceptBooking(request,did):
    data=tbl_coursebooking.objects.get(id=did)
    data.cbooking_status=1
    data.save()
    return redirect("Freelancer:ViewCourseBooking")

def RejectBooking(request,did):
    data=tbl_coursebooking.objects.get(id=did)
    data.cbooking_status=2
    data.save()
    return redirect("Freelancer:ViewCourseBooking")

def logout(request):
    if 'fid' in request.session:
        del request.session['fid']
        return redirect('Guest:Index')
    else:
        return redirect('Guest:Index')     