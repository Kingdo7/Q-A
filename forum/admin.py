from django.contrib import admin

# Register your models here.
from .models import Question, Tag, Answer

# QuestionVote, #AnswerVote
class QuestionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'date_creation', 'id']

class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_creation']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'date_creation', 'id', 'question', 'profile', 'id']
#class QuestionVoteAdmin(admin.ModelAdmin):
#    list_display = ['question', 'profile', 'date_creation']

#class AnswerVoteAdmin(admin.ModelAdmin):
#    list_display = ['answer', 'profile']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin )
admin.site.register(Answer, AnswerAdmin)




#admin.site.register(QuestionVote, QuestionVoteAdmin )

#admin.site.register(AnswerVote, AnswerVoteAdmin )