import datetime

from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth import logout
# Pour gérer les permissions
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, TemplateView
from django.contrib.auth.models import AbstractUser, Group

from .forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm

from django.contrib.auth.models import AbstractUser, Group

from .models import User, Profile, Friend

from . import forms


# Create your views here.

# I
# Authentification formulaire

# def SignupPage(request):
#    form = forms.SignupForm()
#    if request.method == 'POST':
#        form = forms.SignupForm(request.POST)
#        if form.is_valid():
#            user = auto.save()
#            login(request, user)
#            return redirect(setting.LOGIN_REDIRECT_URL)
#
#    return render(request, 'templates/signup.html', context = {'form' : form})
class Index(TemplateView):
    template_name = 'home.html'


def FriendSetter(request, *args, **kwargs):
    priorURL = request.META.get('HTTP_REFERER')
    qs = Profile.objects.get(id=kwargs['pk'])
    # cliq sur test 1 profile = test_1
    #
    if qs.user not in request.user.friendlist.friend.all():
        request.user.friendlist.friend.add(qs.user)
    else:
        request.user.friendlist.friend.remove(qs.user)

    return redirect(priorURL)


def FollowSetter(request, *args, **kwargs):
    priorURL = request.META.get('HTTP_REFERER')
    qs = Profile.objects.get(id=kwargs['pk'])
    # cliq sur test 1 profile = test_1
    #
    if qs.user not in request.user.userprofile.friendlist.all():
        request.user.userprofile.following.add(qs.user)
        qs.follower.add(request.user)
    else:
        request.user.userprofile.following.remove(qs.user)
        qs.follower.remove(request.user)

    return redirect(priorURL)


class UserCreateView(View):
    def get(self, request):
        context = {}
        context['form'] = UserRegistrationForm()  # equivaut à context = {'form': UserLoginForm()}

        return render(request, 'account/signup.html', context)
        # template_name=self.html_template

        # return render(request, 'account/signin.html', context)
        return render(request, 'signup.html', context)

    # template_name=self.html_template
    def post(self, request):
        context = {}
        context['form'] = UserRegistrationForm()
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if email == '':
            messages.error(request, "vous n'avez pas renseigné de mail")
        elif username == '':
            messages.error(request, "vous n'avez pas renseigné d'usurname")
        elif password1 == '':
            messages.error(request, "vous n'avez pas renseigné de mot de passe1")
        elif password2 == '':
            messages.error(request, "vous n'avez pas renseigné de mot de passe1")
        elif password1 != password2:
            messages.error(request, "Vos mots de passe sont différents")
        if User.objects.filter(username=username).exists():
            messages.error(request, "le nom d'utilisateur existe déjà")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "le nom d'utilisateur existe déjà")
        else:
            user = User.objects.create_user(username=username, password=password1, email=email)
            # attribution du groupe quand la perosnne crée le compte. le groupe visitor existe déjàç en admin.
            # group = Group.objects.get(name='visitor')
            # user.groups.add(group)
            auth.login(request, user)
            return redirect('account:index')

        '''return render(request, 'account/signin.html', context)
    def createProfile(sender, **kwargs):
        print("hello")'''

        return render(request, 'account/signup.html', context)


class UserLoginView(View):
    html_template = 'login.html'

    def get(self, request):
        context = {}
        context['form'] = UserLoginForm()
        return render(request, self.html_template, context)

    def post(self, request):
        context = {}
        context['form'] = UserLoginForm()
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            messages.errors(request, "vous n'avez pas renseigné d'usurname")
            return render(request, self.html_template, context)
        elif password == '':
            messages.errors(request, "vous n'avez pas renseigné de mot de passe")
            return render(request, self.html_template, context)
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Vous avez été connecté avec succés")
                # group = Group(name="pdg")
                # if user.groups.filter(name=group):
                #    print("caca")
                #    return redirect('redacteur:redacteur-connect')

                return redirect('account:index')

            else:
                messages.error(request, "Vous n'avez pas pu être connecté")
                return render(request, self.html_template, context)


class UserLogoutView(View):
    def get(self, request):
        if not request.user.is_anonymous:
            messages.error(request, "vous avez été deco")
            logout(request)
            return redirect('/')
        else:
            messages.error(request, "vous n'avez pas été déco")
            return redirect('/')


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "account/profile_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = "account/profile_details.html"


class ProfileListView(ListView):
    model = Profile
    template_name = "account/profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        return context


class ProfileRefreshListView(ListView):
    model = Profile
    template_name = "account/profile_list.html"

    # juliereturn redirect('/')


class FriendListView(ListView):
    model = Friend
    template_name = "account/friend_list.html"


class FriendUpdateView(UpdateView):
    model = Friend
    form_class = ProfileUpdateForm
    template_name = "account/profile_update.html"


class FriendDetailsView(DetailView):
    model = Friend
    template_name = "account/profile_details.html"


class FriendCreateView(CreateView):
    model = Friend
    template_name = "account/friend_create.html"


def AddFriendRelationship(request, *args, **kwargs):
    object = Profile.objects.get(pk=kwargs['pk'])
    friend_recto = Friend.objects.create(
        profile=request.user.userprofile,
        friend=object.user,
    )
    friend_verso = Friend.objects.create(
        profile=object,
        friend=request.user,
    )
    object.waitinglist.add(request.user)
    url = reverse_lazy('account:profile-list')
    return redirect(url)


def RemoveFriendRelationship(request, *args, **kwargs):
    qs1 = Friend.objects.get(friend=User.objects.get(pk=kwargs['pk']), profile=request.user.userprofile)
    qs1.delete()
    qs2 = Friend.objects.get(friend=request.user, profile=User.objects.get(pk=kwargs['pk']).userprofile)
    qs2.delete()
    url = reverse_lazy('account:profile-list')
    return redirect(url)


def AcceptedButton(self):
    # si utilisateur 1 ajoute utilisateur deux
    # dans la page profile /me de l'utilisateur 2
    # on doit avoir la liste des gens qui essaye d'ajouter en amis utilsateur 2
    # je passe les deux relation en accépter is_accepted = True
    # pop de la liste de l'utilisateur 2 le nom de la personne qu'il accepte
    pass
