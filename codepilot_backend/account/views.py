from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from account.serializers import AdminSerializer,StudentSerilaizer

# Create your views here.
class AdminCreateView(CreateAPIView):

    serializer_class = AdminSerializer

class StudentCreateView(CreateAPIView):

    serializer_class = StudentSerilaizer



