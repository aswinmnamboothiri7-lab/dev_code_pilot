from django.urls import path
from question.views import QuestionListCreateView,QuestionRetrieveUpdateDeleteView


urlpatterns = [

    path('assessments/<int:pk>/problem/',QuestionListCreateView.as_view()),

    path('problem/',QuestionListCreateView.as_view()),
    path('problem/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),
    
]