from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import CreateQuestion, DetailsQuestion
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import QuestionModel, Answer
from django.urls import reverse_lazy
from django.contrib import messages

## Convention de nommage

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
    context['query'] = QuestionModel.objects.filter(id=pk)
    context['answer'] = DetailsQuestion(request.POST or None)
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

