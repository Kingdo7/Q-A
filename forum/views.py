from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import CreateQuestion, Details
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import Question, Answer
from django.urls import reverse_lazy
from django.contrib import messages


class QuestionListView(ListView):
    model = Question
    template_name = "Feed.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Feed'] = Question.objects.all()
        return context

class QuestionDetailView(DetailView):
    model = Question
    template_name = "Detail.html"

    def get_context_data(self, **kwargs):
        #pas comprendre la ligne suivante , juste copier coller.
        context = super().get_context_data(**kwargs)
        context['reponse'] = Answer.objects.filter(question__id=self.get_object().id)

        return context





# Create your views here.
def Create(request):
    html_template = "Question.html"
    context = {}
    form = CreateQuestion(request.POST or None)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, html_template, context)


def List(request):
    html_template = "Feed.html"
    context = {}
    context['dataset'] = Question.objects.all()

    return render(request, html_template, context)


#def Details(request, id):
#    html_template = "Detail.html"
#    context = {}
#    context['data'] = Question.objects.get(id=id)
#    form = Details(request.POST or None)
#    context['form'] = form
#    return render(request, html_template, context)


def Update(request, id):
    html_template = "Update.html"
    context = {}
    obj = get_object_or_404(Question, id = id)
    form = CreateQuestion(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context['form'] = form

    return render(request, html_template, context)

class C_Question(CreateView):
    model = Question
    html_template = "Question.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = CreateQuestion()
        return render(request, self.html_template, context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = CreateQuestion(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        context['form'] = form
        return render(request, self.html_template, context)

class D_Question(DetailView):
    model = Question
    html_template = "Detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Question.objects.get(id=id)
        return context


class L_Question(ListView):
    model = Question
    html_template = "Feed.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['dataset'] = Question.objects.all()
        return render(request, self.html_template, context)

class U_Question(UpdateView) :
    model = Question
    html_template = "Update.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = Update()
        return render(request, self.html_template, context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = Update(request.POST or None, id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context['form'] = form
        return render(request, self.html_template, context)

