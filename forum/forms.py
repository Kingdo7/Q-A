from django.forms import ModelForm
from .models import ModelQuestion

class CreateQuestion(ModelForm):
    class Meta:
        model = ModelQuestion
        fields = ['title', 'question']

