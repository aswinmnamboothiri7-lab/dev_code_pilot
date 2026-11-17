from django.urls import path

from assessments.views import AssessmentListCreateView,AssessmentRetrieveUpdateDeleteView,AssessmentPublishView


urlpatterns = [
    path("exam/",AssessmentListCreateView.as_view()),
    path("exam/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
    path("exam/<int:pk>/publish/",AssessmentPublishView.as_view()),
    

]