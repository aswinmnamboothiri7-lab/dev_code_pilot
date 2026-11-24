from django.shortcuts import render,get_object_or_404

# Create your views here.
from submissions.models import Submission

from assessments.models import Assessment




from submissions.serializers import SubmissionSerializer 

from rest_framework import authentication,permissions

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView

from submissions.permissions import OwnerOnly
# from assessments.permissions import AdminOnly
from submissions.permissions import SubmissionAdminOnly

from rest_framework.response import Response



# class SubmissionCreateView(CreateAPIView):

#     serializer_class = SubmissionSerializer

#     authentication_classes = [authentication.TokenAuthentication]

#     # permission_classes = [permissions.IsAuthenticated]
#     permission_classes=[OwnerOnly]

#     def perform_create(self, serializer):

#         # assessment_id = self.request.data.get('assessment')

#         # assessment = Assessment.objects.get(id=assessment_id)

#         # serializer.save(
#         #     student=self.request.user,
#         #     assessment=assessment
#         # )
#         return serializer.save(student=self.request.user)


class SubmissionCreateView(CreateAPIView):

    serializer_class = SubmissionSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [OwnerOnly]

    def perform_create(self, serializer):

        assessment_id = self.kwargs.get('pk')

        assessment = get_object_or_404(Assessment, id=assessment_id)

        serializer.save(
            student=self.request.user,
            assessment=assessment
        )


    

class SubmissionListView(ListAPIView):

    serializer_class=SubmissionSerializer

    queryset=Submission.objects.all()

    
    authentication_classes=[authentication.TokenAuthentication]
    
    permission_classes=[SubmissionAdminOnly]

   


class SubmissionRetrieveView(RetrieveAPIView):

    serializer_class = SubmissionSerializer

    queryset = Submission.objects.all()

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    permission_classes = [SubmissionAdminOnly]

class SubmissionStatusView(RetrieveAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

    def get(self,request,pk):

        try:
            submission=Submission.objects.get(id=pk,student=request.user)

            return Response({
                "submission_id": submission.pk,
                "status": submission.status
            })
        except Submission.DoesNotExist:
            return Response({
                 "message": "Assessment not submitted yet"
            })

class SubmissionFinalAssessmentView(CreateAPIView):
    serializer_class = SubmissionSerializer

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    def post(self,request,pk):

        try:
            submission=Submission.objects.get(id=pk,student=request.user)

            submission.status="submitted"
            submission.save()

            return Response({
                "message": "Assessment submitted successfully",
                "status": submission.status

            })
        except Submission.DoesNotExist:
            return Response({
                "message": "Submission not found"
            })


class SubmissionEvaluateView(RetrieveAPIView):

    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [SubmissionAdminOnly]

    def post(self, request, pk):

        try:
            submission = Submission.objects.get(id=pk)

            submission.marks = request.data.get("marks")
            submission.feedback = request.data.get("feedback")
            submission.status = "evaluated"

            submission.save()

            return Response({
                "message": "Assessment evaluated successfully",
                "submission_id": submission.pk,
                "marks": submission.marks,
                "feedback": submission.feedback,
                "status": submission.status
            })

        except Submission.DoesNotExist:

            return Response({
                "message": "Submission not found"
            })

            
        







