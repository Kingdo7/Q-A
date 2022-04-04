from django.forms import ModelForm
from .models import QuestionModel


class CreateQuestion(ModelForm):
    class Meta:
        model = QuestionModel
        fields = ['titre', 'question']  

class DetailsQuestion(ModelForm):
    class Meta:
        model = QuestionModel
        fields = ['reponse']


