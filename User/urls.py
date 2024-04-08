from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('SearchMusicBand/',views.SearchMusicBand,name="SearchMusicBand"), 
    path('Ajaxband/',views.Ajaxband,name="Ajaxband"), 
    path('ViewWorks/<int:bid>',views.ViewWorks,name="ViewWorks"), 
    path('Ajaxwork/',views.Ajaxwork,name="Ajaxwork"), 
    path('Bandbooking/<int:wid>',views.Bandbooking,name="Bandbooking"),
    path('ViewMyBandbooking/',views.ViewMyBandbooking,name="ViewMyBandbooking"),
    path('BandPay/<int:did>',views.BandPay,name="BandPay"),
    path('SearchCourse/',views.SearchCourse,name="SearchCourse"),
    path('AjaxCourse/',views.AjaxCourse,name="AjaxCourse"), 
    path('Bookcourse/<int:did>',views.Bookcourse,name="Bookcourse"),
    path('ViewCourseBooking/',views.ViewCourseBooking,name="ViewCourseBooking"),
    path('CPay/<int:did>',views.CPay,name="CPay"),
    path("Complaint/",views.Complaint,name="Complaint"),
    path("Delcomplaint/<int:did>", views.Delcomplaint,name="Delcomplaint"),
    path("Feedback/",views.Feedback,name="Feedback"),
    path("Delfeedback/<int:did>", views.Delfeedback,name="Delfeedback"),

    path("logout/",views. logout,name="logout"),
]