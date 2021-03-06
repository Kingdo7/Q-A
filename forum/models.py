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
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='auteur')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name="questiontag")
    #profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='auteur')
    #tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name="questiontag")
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=15000)
    slug = models.SlugField(null=True, blank=True)
    votelist = models.ManyToManyField(Profile, blank=True, related_name="votequestionlist")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return str(self.title) or ""

    def get_absolute_url(self):
        return reverse('question:question-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug:
            super(Question, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title + get_random_string(9))
            super(Question, self).save(*args, **kwargs)

    def get_vote_list_count(self):
        return len(self.votelist.all())

#class QuestionVote(models.Model):
#    answer = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questionvote")
#    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="userquestionvote")
#    date_creation = models.DateTimeField(auto_now_add=True)
#    slug = models.SlugField(null=True, blank=True)
#
#    def __str__(self):
#        return str(self.profile) or ""
#
#    def get_absolute_url(self):
#        return reverse('forum:questionvote-detail',
#                       kwargs={'pk': self.pk})
#
#    def save(self, *args, **kwargs):
#        if self.slug:
#            super(QuestionVote, self).save(*args, **kwargs)
#        else:
#            self.slug = slugify(get_random_string(12))
#            super(QuestionVote, self).save(*args, **kwargs)

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questionanswer")
    #profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="useranswer")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='auteuranswer')
    answer = models.CharField(max_length=2000)
    date_creation = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    votelist = models.ManyToManyField(Profile, blank=True, related_name="voteanswerslist")



    def __str__(self):
        return str(self.author) or ""

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

    def get_vote_list_count(self):
        return len(self.votelist.all())

class QuestionModel(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='Author')
    titre = models.CharField(max_length=50)
    question = models.TextField()
    reponse = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name="questiontag")
    #visit_counter = models.PositiveIntegerField(default=0)
    #liked = models.ManyToManyField(User)

    class Meta :
        ordering = ['updated', 'created']

    def __str__(self):
        return self.titre
