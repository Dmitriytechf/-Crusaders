from django.urls import path
from questions.views import *


urlpatterns = [
    path('', QuestionListView.as_view(), name='test_list'),
    path('test/<int:test_id>/', quiz_view,  name='quiz'),
]