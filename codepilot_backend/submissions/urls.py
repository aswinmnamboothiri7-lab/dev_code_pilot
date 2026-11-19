from django.urls import path

from submissions.views import SubmissionCreateView,SubmissionListView,SubmissionRetrieveView,SubmissionStatusView,SubmissionFinalAssessmentView,SubmissionEvaluateView

urlpatterns = [
    path("assessments/<int:pk>/submit/",SubmissionCreateView.as_view()),
    path("submit/",SubmissionListView.as_view()),
    path("submit/<int:pk>/",SubmissionRetrieveView.as_view()),
    path("submit/<int:pk>/status/",SubmissionStatusView.as_view()),
    path("submit/<int:pk>/final/",SubmissionFinalAssessmentView.as_view()),
    path("submit/<int:pk>/evaluate/",SubmissionEvaluateView.as_view()),
    
    
    
]