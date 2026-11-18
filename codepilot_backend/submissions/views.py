from django.shortcuts import render

# Create your views here.
from submissions.models import Submission

from assessments.models import Assessment

from submissions.serializers import SubmissionSerializer 

from rest_framework import authentication,permissions

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView

from submissions.permissions import OwnerOnly
from assessments.permissions import OwnerOnly

class SubmissionCreateView(CreateAPIView):
    serializer_class=SubmissionSerializer

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    def perform_create(self, serializer):
        return serializer.save(student=self.request.user)

class SubmissionListView(ListAPIView):
    serializer_class=SubmissionSerializer

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    def get_queryset(self):
        return Assessment.objects.filter(creator=self.request.user)

class SubmissionRetrieveView(RetrieveAPIView):
    serializer_class=SubmissionSerializer

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    def get_queryset(self):
        return Assessment.objects.filter(creator=self.request.user)





