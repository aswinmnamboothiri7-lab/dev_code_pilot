from django.shortcuts import render
from answer.models import  Answer
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView
from answer.models import Answer
from answer.serializers import AnswerSerializer
from rest_framework import authentication,permissions
from assessments.permissions import OwnerOnly
# Create your views here.
class AnswerCreateView(CreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]
    serializer_class=AnswerSerializer

class AnswerListView(ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]
    queryset=Answer.objects.all()


class AnswerUpdateView(UpdateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]
    
    serializer_class=AnswerSerializer

    queryset=Answer.objects.all()

    # def get_object(self):
    #     return Answer.objects.get()


