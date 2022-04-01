from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import CreateQuestion
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import QuestionModel, Answer
from django.urls import reverse_lazy
from django.contrib import messages


#class QuestionListView(ListView):
#    model = Question
#   template_name = "Feed.html"
#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['Feed'] = Question.objects.all()
#       return context

#lass QuestionDetailView(DetailView):
#   model = Question
#   template_name = "Detail.html"

#   def get_context_data(self, **kwargs):
#       #pas comprendre la ligne suivante , juste copier coller.
#       context = super().get_context_data(**kwargs)
#       context['reponse'] = Answer.objects.filter(question__id=self.get_object().id)

#        return context





# Create your views here.
def create(request):
    html_template = "Question.html"
    context = {}
    form = CreateQuestion(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form'] = form
    return render(request, html_template, context)

def list(request):
    html_template = "Feed.html"
    context = {}
    context['dataset'] = QuestionModel.objects.all()
    return render(request, html_template, context)


def details(request, pk):
    html_template = "Detail.html"
    context = {}
    context['data'] = QuestionModel.objects.get(id=pk)
    print(QuestionModel.objects.all())
    return render(request, html_template, context)


#def Update(request, pk):
    #html_template = "Update.html"
    #context = {}
    #obj = get_object_or_404(QuestionModel, id = pk)
    #form = CreateQuestion(request.POST or None, instance=obj)
    #if form.is_valid():
        #form.save()
        #return HttpResponseRedirect("/" + id)
    #context['form'] = form
    #return render(request, html_template, context)
