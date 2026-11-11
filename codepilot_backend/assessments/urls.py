from django.urls import path

from assessments.views import AssessmentListCreateView,AssessmentRetrieveUpdateDeleteView


urlpatterns = [
    path("assessment/",AssessmentListCreateView.as_view()),
    path("assessment/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
    

]