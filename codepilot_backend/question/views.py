from django.shortcuts import render
from question.models import Question

# Create your views here.
from question.serializers import QuestionSerializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from assessments.permissions import AdminOnly

class QuestionListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes =[AdminOnly]

    serializer_class = QuestionSerializers

    def get_queryset(self):
        return Question.objects.filter(
            assessment_id=self.kwargs['pk']
        )

    def perform_create(self, serializer):
        return serializer.save()


class QuestionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AdminOnly]

    serializer_class = QuestionSerializers

    queryset = Question.objects.all()
   

    