from django.contrib import admin
from .models import Question


class QuizAdmin(admin.ModelAdmin):
    """ quiz admin docstring """
    list_display = (
        'question_id',
        'question_name',
        'question_description',
        'option1',
        'option2',
        'option3',
        'option4',
        'option5',
        'option6',
        'option7',
        'option8',
        'option9',
        'option10',
        'option11',
        'option12',
        'option13',
        'option14',
        'option15',
    )

    ordering = ('question_name',)


admin.site.register(Question, QuizAdmin)
