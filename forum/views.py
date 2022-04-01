from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import ModelQuestion
from .forms import CreateQuestion
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def Create(request):
    html_template = "forum/templates/Question.html"
    context = {}
    form = CreateQuestion(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, html_template, context)

def List(request):
    html_template = "forum/templates/Feed.html"
    context = {}
    context['dataset'] = ModelQuestion.objects.all()
    return render(request, html_template, context)

def Detail(request, pk):
    html_template = "forum/templates/Detail.html"
    dataset = ModelQuestion.objects.get(id = pk)
    context = {'data' : dataset}
    return render(request, html_template, context)

