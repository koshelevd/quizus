"""Application 'quiz' URL Configuration."""
from django.urls import path, include

from quizus import settings
from . import views


urlpatterns = [
    path('',
         views.index,
         name='index'),
    path('<slug:slug>/congrats/',
         views.congrats,
         name='congrats'),
    path('<slug:slug>/',
         views.show_quiz,
         name='show_quiz'),
]