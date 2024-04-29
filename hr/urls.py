from django.urls import path
from hr import views
urlpatterns = [
    path('hrdash/',views.hrHome,name='hrdash'),
    path('candidatedetails/<int:pk>/',views.hrCandidateDetails,name='candidatedetails'),
    path('postjob/',views.postJobs,name='postjob'),
    path('acceptapplication/',views.acceptApplication,name='acceptapplication'),
    path('rejectapplication/',views.rejectApplication,name='rejectapplication')
     
]
