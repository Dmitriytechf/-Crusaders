from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Test, Question, Answer
from .forms import QuizForm
from django.views.decorators.cache import cache_page


class QuestionListView(ListView):
    """Список всех тестов"""
    model = Test
    template_name = 'quiz/test_list.html'
    context_object_name = 'tests'


# @cache_page(60*5)
def quiz_view(request, test_id):
    """
    View для прохождения теста.
    """
    # Получаем конкретный тест и вопросы к нему
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all().order_by('order')
    
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        
        if form.is_valid():
            # Подсчёт баллов с помощью счетчика
            correct_answers = 0
            user_answers = []
            
            for question in questions:
                # Получаем ID выбранного ответа из cleaned_data
                answer_id = form.cleaned_data.get(f'question_{question.id}')
                user_answer = Answer.objects.get(id=answer_id)
                user_answers.append({
                    'question': question,
                    'answer': user_answer,
                    'is_correct': user_answer.is_correct
                })
                # Увеличиваем счетчик, если ответ правильный 
                if user_answer.is_correct:
                    correct_answers += 1

            # Показываем страницу с результатами
            return render(request, 'quiz/result.html', {
                'test': test,
                'score': correct_answers,
                'total': questions.count(),
                'user_answers': user_answers,
                'percent': int(correct_answers / questions.count() * 100)
            })
    else:
        form = QuizForm(questions=questions)
    
    return render(request, 'quiz/quiz.html', {
        'test': test,
        'form': form,
    })
