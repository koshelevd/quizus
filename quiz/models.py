"""Contains models to provide an Object-relational Mapping in 'posts' app."""
from django.db import models


class Quiz(models.Model):
    """Stores a single quiz entry."""

    title = models.CharField(
        max_length=200,
        verbose_name='Название викторины',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание викторины',
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        verbose_name='ЧПУ',
    )
    success_page = models.FileField(
        upload_to='pages/',
        blank=True,
        null=True,
        verbose_name='Страница с поздравлением',
    )
    image = models.ImageField(
        upload_to='quiz_images/',
        blank=True,
        null=True,
        verbose_name='Изображение викторины',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Викторины'
        verbose_name = 'Викторина'

    def __str__(self):
        """Return quiz's info."""
        return (f'Quiz {self.pk}, {self.title}')


class Question(models.Model):
    """Stores a single question entry."""

    content = models.TextField(
        verbose_name='Содержание вопроса',
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Викторина',
    )
    image = models.ImageField(
        upload_to='questions_images/',
        blank=True,
        null=True,
        verbose_name='Изображение вопроса',
    )
    # sort = models.AutoField(
    #     verbose_name='Порядок сортировки',
    # )
    is_input = models.BooleanField(
        default=False,
        verbose_name='Является полем ввода',
    )
    # right_answers = models.ManyToManyField(
    #     'Answer',
    #     blank=True,
    #     related_name='questions',
    #     verbose_name='Правильные ответы',
    # )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'

    def __str__(self):
        """Return question's info."""
        return (f'Question {self.pk}, {self.content}')


class Answer(models.Model):
    """Stores a single answer entry."""

    content = models.CharField(
        max_length=200,
        verbose_name='Ответ',
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос',
    )
    is_right = models.BooleanField(
        default=False,
        verbose_name='Правильный ответ',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'

    def __str__(self):
        """Return answers's info."""
        return (f'Answer {self.pk}, {self.content}')
