from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('', views.view_quiz, name='view_quiz'),
    # path('quiz/<question_id>', views.view_question_id, name='view_question_id'),
    path('add_question/<question_id>/', views.add_question, name='add_question'),
    path('edit_question/<question_id>/', views.edit_question, name='edit_question'),
    path('delete_question/<question_id>/', views.delete_question, name='delete_question'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
