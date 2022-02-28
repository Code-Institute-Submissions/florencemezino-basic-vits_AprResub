from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz'),
    path('add_question/', views.add_question, name='add_question'),
    path('edit_question/', views.edit_question, name='edit_question'),
    path('delete_question/', views.delete_question, name='delete_question'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
