from django.shortcuts import render

from account.models import StudentProfile

from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from account.serializers import AdminSerializer,StudentSerilaizer,StudentProfileSerializer

# Create your views here.
class AdminCreateView(CreateAPIView):

    serializer_class = AdminSerializer

class StudentCreateView(CreateAPIView):

    serializer_class = StudentSerilaizer


class StudentProfileRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

   

    serializer_class = StudentProfileSerializer

    queryset = StudentProfile.objects.all()




