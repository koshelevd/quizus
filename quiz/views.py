"""View functions of the Posts app."""
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Quiz


def index(request):
    """
    Display all quizes :model:'quiz.Quiz' on the main page.
    """
    quiz_list = Quiz.objects.all()

    return render(
        request,
        'quiz/index.html',
        {
            'quiz_list': quiz_list,
        }
    )


def show_quiz(request, slug):
    """
    Display 'quiz.Quiz' with 'quiz.Question', check 'quiz.Answer'.
    """
    next = request.POST.get('next')
    question_index = int(request.POST.get('question_index', 1))
    if next is not None: question_index = int(next) + 1
    quiz = get_object_or_404(Quiz, slug=slug)
    if quiz.questions.all().count() == 0:
        return render(request, 'quiz/quiz.html', {'quiz': quiz})
    questions = quiz.questions.all()
    count = questions.count()
    context = {
        'quiz': quiz,
        'question_index': question_index,
        'count': count,
    }

    if request.method == 'POST' and next is None:
        question_pk = int(request.POST.get('question_pk'))
        question = quiz.questions.get(pk=question_pk)
        context['question'] = question
        user_answers_pks = []
        right_answers_pks = []

        if not question.is_input:
            for key, value in request.POST.items():
                if 'answer-' in key and value == 'on':
                    user_answers_pks.append(int(key[7:]))
            for answer in question.answers.all():
                if answer.is_right:
                    right_answers_pks.append(answer.pk)
            result = user_answers_pks == right_answers_pks
            right_answers = [answer.content for answer in
                             question.answers.all() if
                             answer.pk in right_answers_pks]
            user_answers = [answer.content for answer in question.answers.all()
                            if answer.pk in user_answers_pks]
        else:
            user_input = request.POST.get('input-field')
            for answer in question.answers.all():
                result = answer.content == user_input
            user_answers = [user_input]
            right_answers = [answer.content]



        context['result'] = result
        context['right_answers'] = ', '.join(right_answers)
        context['user_answers'] = ', '.join(user_answers)
        return render(request, 'quiz/quiz.html', context)

    for index, question in enumerate(questions):
        if index == question_index - 1: break;

    answers = [(index + 1, answer) for index, answer in enumerate(
        question.answers.all())]
    context['question'] = question
    if len(answers) > 1: context['answers'] = answers

    return render(request, 'quiz/quiz.html', context)


def congrats(request, slug):
    """
    Display result page.
    """
    quiz = get_object_or_404(Quiz, slug=slug)
    if quiz.success_page is not None:
        return HttpResponse(quiz.success_page)
    return render(request, 'quiz/congrats.html', {})
