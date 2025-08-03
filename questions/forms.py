from django import forms
from .models import Test, Question, Answer
from django.utils.safestring import mark_safe



class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # Получаем вопросы теста через questions
        self.questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        
        
        for question in self.questions:
            answers = question.answers.all() # Получаем все варианты ответов через related_name
            label = question.text
            
            # Обработка изображение, если оно есть.
            if question.image:
                label = mark_safe(f"""
                <div class="question-content">
                    <div class="image-container d-flex justify-content-center">
                        <img src="{question.image.url}" 
                            class="img-fluid rounded shadow-lg" 
                            style="max-height: 500px; width: auto;"
                            alt="Изображение к вопросу">
                    </div>
                    <p class="fs-4 mb-4">{question.text}</p>
                </div>
                """)
            else:
                label = mark_safe(f'<p class="fs-4">{question.text}</p>')
            
            # создаем поле с уникальным именем, включающим ID вопроса
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                # поля которые мы включаем в вопрос по условию выше
                label=label,
                # варианты ответов в формате
                choices=[(answer.id, answer.text) for answer in answers],
                # виджет радиокнопок для выбора одного варианта
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                # поле обязательно для заполнения
                required=True,
                error_messages={
                    'required': 'Пожалуйста, выберите ответ.'
                }
            )
