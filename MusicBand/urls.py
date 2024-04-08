from django.urls import path,include
from MusicBand import views
app_name="musicband"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('Bandworks/',views.Bandworks,name="Bandworks"),
    path('delBandworks/<int:did>',views.delBandworks,name="delBandworks"),
    path('BandGallery/<int:gid>',views.BandGallery,name="BandGallery"),
    path('delwork/<int:did>',views.delwork,name="delwork"),
    path('ViewUserBooking/',views.ViewUserBooking,name="ViewUserBooking"),
    path('AcceptBooking/<int:did>',views.AcceptBooking,name="AcceptBooking"),
    path('RejectBooking/<int:did>',views.RejectBooking,name="RejectBooking"),
    path('Amount/<int:did>',views.Amount,name="Amount"),

    path("logout/",views. logout,name="logout"),
]