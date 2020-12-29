"""Application 'quiz' admin page configuration."""
from django.contrib import admin

from .models import Answer, Question, Quiz


class QuestionsInline(admin.StackedInline):
    model = Question.quiz.through
    extra = 0


class AnswersInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """Manage quizes."""

    list_display = (
        'pk',
        'title',
        'slug',
        'description',
        'image',
        'success_page',
    )
    search_fields = (
        'title',
        'slug',
    )
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('title',)}
    inlines = (QuestionsInline,)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Manage questions."""

    list_display = (
        'pk',
        'content',
        'is_input',
        'image',
    )
    # exclude = ('quiz',)
    list_filter = ('quiz',)
    search_fields = (
        'quiz',
        'content',
    )
    empty_value_display = '-пусто-'
    inlines = (AnswersInline,)


# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     """Manage answers."""
#
#     list_display = (
#         'pk',
#         'question',
#         'content',
#     )
#     list_filter = ('question',)
#     search_fields = (
#         'question',
#         'content',
#     )
#     empty_value_display = '-пусто-'
