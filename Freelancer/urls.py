from django.urls import path,include
from Freelancer import views
app_name="Freelancer"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('Course/',views.Course,name="Course"),
    path('delcourse/<int:did>',views.delcourse,name="delcourse"),
    path('Gallery/',views.Gallery,name="Gallery"),
    path('delgallery/<int:did>',views.delgallery,name="delgallery"),
    path('ViewCourseBooking/',views.ViewCourseBooking,name="ViewCourseBooking"),
    path('AcceptBooking/<int:did>',views.AcceptBooking,name="AcceptBooking"),
    path('RejectBooking/<int:did>',views.RejectBooking,name="RejectBooking"),

    path("logout/",views. logout,name="logout"),
]