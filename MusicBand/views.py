from django.shortcuts import render,redirect
from Guest.models import *
from MusicBand.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"musicband/HomePage.html")

def my_pro(request):
    data=tbl_MusicalBandRegistration.objects.get(id=request.session["mid"])
    return render(request,"musicband/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_MusicalBandRegistration.objects.get(id=request.session["mid"])
    if request.method=="POST":
        prodata.MusicalBandRegistration_name=request.POST.get('txtname')
        prodata.MusicalBandRegistration_contact=request.POST.get('txtcon')
        prodata.MusicalBandRegistration_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"musicband/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"musicband/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_MusicalBandRegistration.objects.filter(id=request.session["mid"],MusicalBandRegistration_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                musicbanddata=tbl_MusicalBandRegistration.objects.get(id=request.session["mid"],MusicalBandRegistration_password=request.POST.get('txtcurpass'))
                musicbanddata.MusicalBandRegistration_password=request.POST.get('txtnewpass')
                musicbanddata.save()
                return render(request,"musicband/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"musicband/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"musicband/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"musicband/ChangePassword.html")

def Bandworks(request):
    data=tbl_Musicaltype.objects.all()
    band=tbl_MusicalBandRegistration.objects.get(id=request.session["mid"])
    work=tbl_Bandworks.objects.filter(musicband=band)
    if request.method=="POST":
        seltype=tbl_Musicaltype.objects.get(id=request.POST.get("typedrp"))
        tbl_Bandworks.objects.create(Bandworks_details=request.POST.get("txt_type"),
                                    Bandworks_files=request.FILES.get("files"),
                                    musicaltype=seltype,
                                    musicband=band)
        return redirect("musicband:Bandworks")
    else:
        return render(request,"Musicband/Bandworks.html",{'data':data,'work':work})

def delBandworks(request,did):
    tbl_Bandworks.objects.get(id=did).delete()
    return redirect("musicband:Bandworks")

def BandGallery(request,gid):
    work=tbl_Bandworks.objects.get(id=gid)
    data=tbl_BandGallery.objects.filter(bandwork=work)
    if request.method=="POST":
        tbl_BandGallery.objects.create(BandGallery_files=request.FILES.get("files"),
                                        BandGallery_caption=request.POST.get("txt_gallerycaption"),
                                        bandwork=work)
        return redirect("musicband:BandGallery",gid=gid)
    else:
        return render(request,"musicband/BandGallery.html",{'data':data})
def delwork(request,did):
    tbl_BandGallery.objects.get(id=did).delete()
    return redirect("musicband:Bandworks")


def ViewUserBooking(request):
    band=tbl_MusicalBandRegistration.objects.get(id=request.session["mid"])
    data=tbl_bandbooking.objects.filter(bandwork__musicband=band)
    return render(request,"musicband/ViewUserBooking.html",{'data':data})

def AcceptBooking(request,did):
    data=tbl_bandbooking.objects.get(id=did)
    data.booking_status=1
    data.save()
    return redirect("musicband:ViewUserBooking")

def RejectBooking(request,did):
    data=tbl_bandbooking.objects.get(id=did)
    data.booking_status=2
    data.save()
    return redirect("musicband:ViewUserBooking")

def Amount(request,did):
    data=tbl_bandbooking.objects.get(id=did)
    if request.method=="POST":
        data.booking_amount=request.POST.get("txtamnt")
        data.save()
        return redirect("musicband:ViewUserBooking")
    else:
        return render(request,"musicband/Amount.html")
    
def logout(request):
    if 'mid' in request.session:
        del request.session['mid']
        return redirect('Guest:Index')
    else:
        return redirect('Guest:Index')     