from django.contrib import admin
from .models import Test, Question, Answer


# Отображение ответо в табличнов виде
class  AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    min_num = 2
    fields = ['text', 'is_correct', 'explanation']
    ordering = ['id']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'test', 'order'] # поля, отображаемые в списке вопросов
    list_filter = ['test']
    search_fields = ['text']
    inlines = [AnswerInline]
    ordering = ['test', 'order']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
