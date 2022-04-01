from django.urls import path
from . import views


app_name = 'forum'


urlpatterns = [
    path("create/", views.create, name = "Question"),
    #path("<str:pk>/update", views.Update, name="update"),
    path("detail/<str:pk>/", views.details, name="details"),
    path("", views.list, name='feed'),

]
