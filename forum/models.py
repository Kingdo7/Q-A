from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from django.utils.crypto import get_random_string
#Permet d'avoir dans article en admin, de mettre du contenu en mode word/html
from django.utils.text import slugify

# Create your models here.
from django.db.models import DateTimeField
from account.models import Profile

class Tag(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.slug) or ""

    def get_absolute_url(self):
        return reverse('account:tag-detail', kwargs={'pk': self.pk})


    def save(self, *args, **kwargs):
        if self.slug:
            super(Tag, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)
            super(Tag, self).save(*args, **kwargs)


class Question(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='auteur')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name="questiontag")
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=15000)
    #visit_counter = models.PositiveIntegerField(default=0)
    #liked = models.ManyToManyField(User)
    slug = models.SlugField(null=True, blank=True)
    votelist = models.ManyToManyField(Profile, blank=True,  related_name="votequestionlist")
    def __str__(self):
        return str(self.title) or ""


    def get_absolute_url(self):
        return reverse('account:account-detail',
                       kwargs={'pk': self.pk}
                       )

    def save(self, *args, **kwargs):
        if self.slug:
            super(Question, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title + get_random_string(9))
            super(Question, self).save(*args, **kwargs)

    def get_vote_list_count(self):
        return len(self.votelist.all())


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questionanswer")
    profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="useranswer")
    answer = models.CharField(max_length=2000)
    date_creation = models.DateTimeField(auto_now_add=True)
    votelist = models.ManyToManyField(Profile, blank=True,  related_name="voteanswerslist")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.profile) or ""

    def get_absolute_url(self):
        return reverse('forum:answer-detail',
                       kwargs={'pk': self.pk}
                       )

    def save(self, *args, **kwargs):
        if self.slug:
            super(Answer, self).save(*args, **kwargs)
        else:
            self.slug = slugify(get_random_string(12))
            super(Answer, self).save(*args, **kwargs)


class AnswerVote(models.Model):

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="answervote")
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="useranswervote")
    date_creation = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.profile) or ""

    def get_absolute_url(self):
        return reverse('forum:answervote-detail',
                       kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.slug:
            super(AnswerVote, self).save(*args, **kwargs)
        else:
            self.slug = slugify(get_random_string(12))
            super(AnswerVote, self).save(*args, **kwargs)


class Question_model(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="Author")
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(null=True, blank=True)

    #visit_counter = models.PositiveIntegerField(default=0)
    #liked = models.ManyToManyField(User)

    def __str__(self):
        return str(self.title) or ""


    def get_absolute_url(self):
        return reverse('forum:details',
                       kwargs={'id': self.slug}
                       )

    def save(self, *args, **kwargs):
        if self.slug:
            super(Question_model, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title + get_random_string(9))
            super(Question_model, self).save(*args, **kwargs)



