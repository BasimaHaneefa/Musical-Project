from django.urls import path,include
from Admin import views
app_name="webadmin"
urlpatterns = [

    path('home/',views.Home,name="AdminHome"),

    path('District/',views.District, name="District"),
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('Updatedis/<int:uid>',views.Updatedis,name="Updatedis"),

  

    path('Place/',views.Place, name="Place"),
    path('deleteplace/<int:did>',views.DeletePlace,name="DeletePlace"),
    path('Updateplace/<int:uid>',views.Updateplace,name="Updateplace"),

    path('MusicalType/',views.MusicalType,name="MusicalType"),
    path('DeleteMusicalType/<int:did>',views.DeleteMusicalType,name="DeleteMusicalType"),
    path('Updatemusicaltype/<int:uid>',views.Updatemusicaltype,name="Updatemusicaltype"),

    path('MusicbandVerification/',views.MusicbandVerification,name="MusicbandVerification"),
    path('AcceptedMusicband/<int:uid>',views.AcceptedMusicband,name="AcceptedMusicband"),
    path('RejectedMusicband/<int:did>',views.RejectedMusicband,name="RejectedMusicband"),
    path('AcceptedMusicbandList/',views.AcceptedMusicbandList,name="AcceptedMusicbandList"),
    path('RejectedMusicbandList/',views.RejectedMusicbandList,name="RejectedMusicbandList"),

    path('FreelancerVerification/',views.FreelancerVerification,name="FreelancerVerification"),
    path('AcceptedFreelancer/<int:uid>',views.AcceptedFreelancer,name="AcceptedFreelancer"),
    path('RejectedFreelancer/<int:did>',views.RejectedFreelancer,name="RejectedFreelancer"),
    path('AcceptedFreelancerList/',views.AcceptedFreelancerList,name="AcceptedFreelancerList"),
    path('RejectedFreelancerList/',views.RejectedFreelancerList,name="RejectedFreelancerList"),

    path("ViewComplaint/",views. ViewComplaint,name="ViewComplaint"),
    path("Reply/<int:rid>",views. Reply,name="Reply"),
    path("ViewFeedback/",views. ViewFeedback,name="ViewFeedback"),

    path("logout/",views. logout,name="logout"),

     
]