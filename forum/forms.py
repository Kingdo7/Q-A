from django.forms import ModelForm
from .models import Question


class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ['title']  #, 'question'


class Details(ModelForm):
    class Meta:
        model = Question
        fields = ['title']
        #fields = ['answer']
