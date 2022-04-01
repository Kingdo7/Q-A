from django.urls import path
from . import views


app_name = 'forum'


urlpatterns = [
    path("create/", views.Create, name = "Question"),
    #path("/<str:pk>/update", views.Update, name="update"),
    path("detail/<str:pk>/", views.Detail, name="details"),
    path("", views.List, name='feed'),

]
