from django.urls import path

from submissions.views import SubmissionCreateView,SubmissionListView,SubmissionRetrieveView

urlpatterns = [
    path("assessments/<int:pk>/submit/",SubmissionCreateView.as_view()),
    path("submit/",SubmissionListView.as_view()),
    path("submit/<int:pk>/",SubmissionRetrieveView.as_view()),
    
]