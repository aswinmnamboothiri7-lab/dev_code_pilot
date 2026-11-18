from django.urls import path
from answer.views import AnswerCreateView,AnswerListView,AnswerUpdateView

urlpatterns=[
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),
    path("submission/<int:pk>/answer/<int:pk>/",AnswerListView.as_view()),
    
]