from django.urls import path

from account.views import StudentCreateView,AdminCreateView
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [

    
    path('admin/register/',AdminCreateView.as_view()),
    path('student/register/',StudentCreateView.as_view()),
    path('student/token/',ObtainAuthToken.as_view()),
    path('admin/token/',ObtainAuthToken.as_view()),

    


  
]
