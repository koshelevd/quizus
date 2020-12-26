"""Application 'quiz' admin page configuration."""
from django.contrib import admin

from .models import Answer, Question, Quiz


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


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Manage questions."""

    list_display = (
        'pk',
        'quiz',
        'content',
        'is_input',
        'image',
    )
    list_filter = ('quiz',)
    search_fields = (
        'quiz',
        'content',
    )
    empty_value_display = '-пусто-'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Manage answers."""

    list_display = (
        'pk',
        'question',
        'content',
    )
    list_filter = ('question',)
    search_fields = (
        'question',
        'content',
    )
    empty_value_display = '-пусто-'