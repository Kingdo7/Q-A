from django.urls import path
from . import views
from .views import (
    C_Question,
    D_Question,
    U_Question,
    L_Question,
    QuestionListView,
    QuestionDetailView,
)

app_name = 'forum'
# path("detail/<int:id>/", views.Details, name="details"),

urlpatterns = [
    path("create/", views.Create, name = "Question"),
    #path("<slug:id>/update", views.Update, name="update"),

    #path("", views.List, name='feed'),
    path('', QuestionListView.as_view(), name="question-list"),
    path('<str:slug>/', QuestionDetailView.as_view(), name="question-detail"),
]
