from django.urls import path
from candidate import views
urlpatterns = [
     path('dash/',views.candidateHome,name='dash'),
     path('applyjob/<int:pk>/',views.applyJob,name='apply'),
     path('applylist/',views.myjoblist,name='mylist')
]
