from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import tbl_complaint, tbl_feedback
# Create your views here.
def Home(request):
    return render(request,"Admin/HomePage.html")

def District(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txt_district"))
        return render(request,"Admin/District.html",{"District":data})
    else:
        return render(request,"Admin/District.html",{"District":data})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("webadmin:District")

def Updatedis(request,uid):
    dis=tbl_district.objects.get(id=uid)
    if request.method=="POST":
        dis.district_name=request.POST.get("txt_district")
        dis.save()
        return redirect("webadmin:District")
    else:
        return render(request,"Admin/District.html",{"disdata":dis})
        

          
def Place(request):
    ddata=tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        seldata=tbl_district.objects.get(id=request.POST.get("district"))
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=seldata)
        return render(request,"Admin/Place.html",{"Place":data,"District":ddata})
    else:
        return render(request,"Admin/Place.html",{"Place":data,"District":ddata})

def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("webadmin:Place")

def Updateplace(request,uid):
    pl=tbl_place.objects.get(id=uid)
    if request.method=="POST":
        pl.place_name=request.POST.get("txt_place")
        pl.save()
        return redirect("webadmin:Place")
    else:
        return render(request,"Admin/Place.html",{"pldata":pl})



def MusicalType(request):
    data=tbl_Musicaltype.objects.all()
    if request.method=="POST":
        tbl_Musicaltype.objects.create(Musical_type=request.POST.get("txt_MusicalType"))
        return render(request,"Admin/MusicalType.html",{"MusicalType":data})
    else:
        return render(request,"Admin/MusicalType.html",{"MusicalType":data})


def DeleteMusicalType(request,did):
    tbl_Musicaltype.objects.get(id=did).delete()
    return redirect("webadmin:MusicalType")

def Updatemusicaltype(request,uid):
    mlt=tbl_Musicaltype.objects.get(id=uid)
    if request.method=="POST":
        mlt.Musical_type=request.POST.get("txt_MusicalType")
        mlt.save()
        return redirect("webadmin:MusicalType")
    else:
        return render(request,"Admin/MusicalType.html",{"mltdata":mlt})

def MusicbandVerification(request):
    msc=tbl_MusicalBandRegistration.objects.filter(MusicalBandRegistration_vstatus=0)
    print(msc)
    return render(request,"Admin/MusicbandVerification.html",{"MusicbandVerification":msc})

def AcceptedMusicband(request,uid):
    acc=tbl_MusicalBandRegistration.objects.get(id=uid)
    acc.MusicalBandRegistration_vstatus=1
    acc.save()
    return redirect("webadmin:AdminHome")
    
        

def RejectedMusicband(request,did):
    rej=tbl_MusicalBandRegistration.objects.get(id=did)
    rej.MusicalBandRegistration_vstatus=2
    rej.save()
    return redirect("webadmin:AdminHome")

def AcceptedMusicbandList(request):
    msc=tbl_MusicalBandRegistration.objects.filter(MusicalBandRegistration_vstatus=1)
    print(msc)
    return render(request,"Admin/AcceptedMusicbandList.html",{"MusicbandVerification":msc})

def RejectedMusicbandList(request):
    msc=tbl_MusicalBandRegistration.objects.filter(MusicalBandRegistration_vstatus=2)
    print(msc)
    return render(request,"Admin/RejectedMusicbandList.html",{"MusicbandVerification":msc})
    

def FreelancerVerification(request):
    flr=tbl_FreelancerRegistration.objects.filter(FreelancerRegistration_vstatus=0)
    print(flr)
    return render(request,"Admin/FreelancerVerification.html",{"FreelancerVerification":flr})

def AcceptedFreelancer(request,uid):
    acc=tbl_FreelancerRegistration.objects.get(id=uid)
    acc.FreelancerRegistration_vstatus=1
    acc.save()
    return redirect("webadmin:AdminHome")

def RejectedFreelancer(request,did):
    rej=tbl_FreelancerRegistration.objects.get(id=did)
    rej.FreelancerRegistration_vstatus=2
    rej.save()
    return redirect("webadmin:AdminHome")

def AcceptedFreelancerList(request):
    flr=tbl_FreelancerRegistration.objects.filter(FreelancerRegistration_vstatus=1)
    print(flr)
    return render(request,"Admin/AcceptedFreelancerList.html",{"FreelancerVerification":flr})

def RejectedFreelancerList(request):
    flr=tbl_FreelancerRegistration.objects.filter(FreelancerRegistration_vstatus=2)
    print(flr)
    return render(request,"Admin/RejectedFreelancerList.html",{"FreelancerVerification":flr})

def ViewComplaint(request):
    newcom=tbl_complaint.objects.filter(complaint_status=0)
    recom=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{'new':newcom,'repl':recom})  
def Reply(request,rid):
    com=tbl_complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("txtpro")
        com.complaint_status=1
        com.save()
        return redirect("webadmin:ViewComplaint")
    else:
        return render(request,"Admin/Reply.html")
def ViewFeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{'data':data})     

def logout(request):
    if 'adid' in request.session:
        del request.session['adid']
        return redirect('Guest:Index')
    else:
        return redirect('Guest:Index')                   

