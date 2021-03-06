from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import (
    QuestionListAPI,
    QuestionDetailAPI,
    QuestionCreateAPI,
    QuestionUpdateAPI,
    QuestionAnswersListAPI,
    AnswerDetailAPI,
    AnswerCreateAPI,
    AddVoteQuestionAPI,
    AddVoteAnswerAPI,
    QuestionListVoteAPI,
    AnswerListVoteAPI,
    ProfileListAPI,
    ProfileDetailAPI,
    ProfileUpdateAPI,
    ProfileDetailConnected,


)




app_name = 'api'


urlpatterns = [



    path('questions/', QuestionListAPI.as_view(), name="question-list"),
    #Ajoute un nouvel enregistrement Question et l'associer à l'utilisateur
    path('questions/create/', QuestionCreateAPI.as_view(), name="question-create"),
    path('questions/<int:pk>/', QuestionDetailAPI.as_view(), name="question-get"),
    path('questions/<int:pk>/update/', QuestionUpdateAPI.as_view(), name="question-update"),

    #Answers
    path('questions/<int:pk>/answers/', QuestionAnswersListAPI.as_view(), name="question-answers"),
    path('answers/create/', AnswerCreateAPI.as_view(), name="answer-create"),
    path('answers/<int:pk>/', AnswerDetailAPI.as_view(), name="answer-get"),

    #Vote
    path('votes/questions/<int:pk>/', AddVoteQuestionAPI.as_view(), name="question-vote"),
    path('votes/answers/<int:pk>/', AddVoteAnswerAPI.as_view(), name="answer-vote"),
    #ListVote
    path('questions/<int:pk>/votes/', QuestionListVoteAPI.as_view(), name="question-listvote"),
    path('answers/<int:pk>/votes/', AnswerListVoteAPI.as_view(), name="answer-listvote"),


    path('profiles/', ProfileListAPI.as_view(), name="profile-list"),
    path('profiles/<int:pk>/', ProfileDetailAPI.as_view(), name="profile-get"),
    path('profiles/<int:pk>/update/', ProfileUpdateAPI.as_view(), name="profile-update"),
    path('me/', ProfileDetailConnected.as_view(), name="profile-connected"),



]