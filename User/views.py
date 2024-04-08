from django.shortcuts import render,redirect
from Freelancer.models import tbl_Course
from Guest.models import *
from Admin.models import *
from MusicBand.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")

def SearchMusicBand(request):
    disdata=tbl_district.objects.all()
    data=tbl_MusicalBandRegistration.objects.filter(MusicalBandRegistration_vstatus=1)
    return render(request,"user/SearchMusicBand.html",{'District':disdata,'data':data})

def Ajaxband(request):
    if request.GET.get("disd") != "" and request.GET.get("pl") != "":
        data=tbl_MusicalBandRegistration.objects.filter(place__district=request.GET.get("disd"),place=request.GET.get("pl"),MusicalBandRegistration_vstatus=1)
        return render(request,"user/AjaxBand.html",{'data':data})
    elif request.GET.get("disd") != "" :
        data=tbl_MusicalBandRegistration.objects.filter(place__district=request.GET.get("disd"),MusicalBandRegistration_vstatus=1)
        return render(request,"user/AjaxBand.html",{'data':data})
    elif request.GET.get("pl") != "":
        data=tbl_MusicalBandRegistration.objects.filter(place=request.GET.get("pl"),MusicalBandRegistration_vstatus=1)
        return render(request,"user/AjaxBand.html",{'data':data})
    else:
        data=tbl_MusicalBandRegistration.objects.filter(MusicalBandRegistration_vstatus=1)
        return render(request,"user/AjaxBand.html",{'data':data})

def ViewWorks(request,bid):
    data=tbl_Musicaltype.objects.all()
    fdata=tbl_MusicalBandRegistration.objects.get(id=bid)
    request.session["fdata"]=fdata.id
    wdata=tbl_Bandworks.objects.filter(musicband=fdata)
    return render(request,"user/ViewWorks.html",{'data':data,'wdata':wdata})

def Ajaxwork(request):
    if request.GET.get("disd") != "":
        data=tbl_Musicaltype.objects.get(id=request.GET.get("disd"))
        wdata=tbl_Bandworks.objects.filter(musicband=request.session["fdata"],musicaltype=data)
        return render(request,"user/Ajaxwork.html",{'wdata':wdata})
    else:
        wdata=tbl_Bandworks.objects.filter(musicband=request.session["fdata"])
        return render(request,"user/Ajaxwork.html",{'wdata':wdata})


def Bandbooking(request,wid):
    wrk=tbl_Bandworks.objects.get(id=wid)
    prodata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_district.objects.all()
    if request.method=="POST":
        pdata=tbl_place.objects.get(id=request.POST.get("placedrp"))
        tbl_bandbooking.objects.create(bandwork=wrk,
                                        booking_venue=request.POST.get("txt_venue"),
                                        user=prodata,
                                        booking_fordate=request.POST.get("date"),
                                        booking_fortime=request.POST.get("time"),
                                        place=pdata)
        return redirect("User:homepage")
    else:
        return render(request,"user/Bandbooking.html",{'District':data})

def ViewMyBandbooking(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_bandbooking.objects.filter(user=prodata)
    return render(request,"user/ViewMyBandbooking.html",{'data':data})

def BandPay(request,did):
    data=tbl_bandbooking.objects.get(id=did)
    if request.method =="POST":
        data.payment_status=1
        data.save()
        return redirect("User:ViewMyBandbooking")
    else:
        return render(request,"user/Payment.html")


def SearchCourse(request):
    mdata=tbl_Musicaltype.objects.all()
    data=tbl_Course.objects.all()
    return render(request,"user/SearchCourse.html",{'data':data,'mdata':mdata})

def AjaxCourse(request):
    if request.GET.get("disd") != "":
        data=tbl_Musicaltype.objects.get(id=request.GET.get("disd"))
        wdata=tbl_Course.objects.filter(musicaltype=data)
        return render(request,"user/AjaxCourse.html",{'data':wdata})
    else:
        wdata=tbl_Course.objects.all()
    return render(request,"user/AjaxCourse.html")

def Bookcourse(request,did):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_Course.objects.get(id=did)
    tbl_coursebooking.objects.create(user=prodata,course=data)
    return redirect("User:ViewCourseBooking")

def ViewCourseBooking(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_coursebooking.objects.filter(user=prodata)
    return render(request,"user/ViewCourseBooking.html",{'data':data})

def CPay(request,did):
    data=tbl_coursebooking.objects.get(id=did)
    if request.method =="POST":
        data.payment_status=1
        data.save()
        return redirect("User:ViewCourseBooking")
    else:
        return render(request,"user/CPayment.html")

def Complaint(request):
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    Complaint=tbl_complaint.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_complaint.objects.create(user=customerdata,
                                    complaint_title=request.POST.get("txttit"),
                                    complaint_content=request.POST.get("txtcomplaint"))
       return redirect("User:Complaint")
    else:
        return render(request,"User/Complaint.html",{'complaint':Complaint}) 

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:Complaint")

def Feedback(request):
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    feedback=tbl_feedback.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_feedback.objects.create(user=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("User:Feedback")
    else:
        return render(request,"User/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:Feedback")   

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('Guest:Index')
    else:
        return redirect('Guest:Index')       