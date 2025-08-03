from django.db import models

class Test(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название теста",
        help_text="Например: 'Рыцарские ордена Европы'"
    )
    description = models.TextField(
        verbose_name="Описание теста",
        blank=True,
        help_text='Здесь должно быть ваше описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания теста'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ['-created_at']


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name="Тест",
        help_text='Связь вопроса с тестом'
    )
    text = models.TextField(verbose_name='текст вопроса')
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядковый номер"
    )
    image = models.ImageField(
        upload_to='questions/',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    
    def __str__(self):
        return f'{self.text[:70]}'
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    questions = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Вопрос"
    )
    text = models.CharField(
        max_length=300,
        verbose_name="Текст ответа"
    )
    is_correct = models.BooleanField(
        default=False,
        verbose_name="Правильный ответ"
    )
    explanation = models.TextField(
        blank=True,
        verbose_name="Пояснение к ответу",
        help_text="Почему этот ответ правильный? (показывается после ответа)"
    )

    def __str__(self):
        return f'{self.text[:70]}'
    
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
